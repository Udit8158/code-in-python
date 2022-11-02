from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Syncronous cryptography

message = b"I am Udit Kundu"  # message in byte format -> so use b infront
# key = Fernet.generate_key()
# f = Fernet(key)

# encry_token = f.encrypt(message)
# print(encry_token)

# print(f.decrypt(encry_token))

# Assyncronous cryptography  -> link of ref ->>>>>>>> https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

# KEY GENERATION


def private_key_gen():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )


def public_key_gen(pr_key):
    return pr_key.public_key()


private_key1 = private_key_gen()
public_key1 = public_key_gen(private_key1)
private_key2 = private_key_gen()
public_key2 = public_key_gen(private_key2)
# print(private_key)
# print(public_key)

# SIGNATURE
signature1 = private_key1.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

signature2 = private_key2.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


# VERIFICATION OF SIGNATURE
try:
    public_key2.verify(
        signature2,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("VARIFICATION SUCCEEDED")
except:
    print("VERIFICATON FAILED")
