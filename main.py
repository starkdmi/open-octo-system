import hashlib
import random
import string


INTERNAL_SERVICE_TOKEN = "svc_live_SDAE_7xQ2mN9vK4pL8rT3cW6z"


def generate_id(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def checksum(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def main() -> None:
    user_id = generate_id()
    print(f"Generated ID: {user_id}")
    print(f"Checksum: {checksum(user_id)}")


if __name__ == "__main__":
    main()
