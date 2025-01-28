#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{decl_event, decl_module, decl_storage, dispatch, ensure};
use frame_system::ensure_signed;
use sp_std::vec::Vec;

pub trait Config: frame_system::Config {
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
}

decl_storage! {
    trait Store for Module<T: Config> as TokenBridge {
        LockedTokens get(fn locked_tokens): map hasher(blake2_128_concat) T::AccountId => u64;
    }
}

decl_event!(
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        TokensLocked(AccountId, u64),
        TokensUnlocked(AccountId, u64),
    }
);

decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        type Error = ();

        fn deposit_event() = default;

        #[weight = 10_000]
        pub fn lock_tokens(origin, amount: u64) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;
            <LockedTokens<T>>::insert(&sender, amount);
            Self::deposit_event(RawEvent::TokensLocked(sender, amount));
            Ok(())
        }

        #[weight = 10_000]
        pub fn unlock_tokens(origin, user: T::AccountId, amount: u64) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;
            ensure!(<LockedTokens<T>>::contains_key(&user), "User has no locked tokens");
            <LockedTokens<T>>::remove(&user);
            Self::deposit_event(RawEvent::TokensUnlocked(user, amount));
            Ok(())
        }
    }
}