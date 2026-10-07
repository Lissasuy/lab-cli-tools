import zipfile
import zlib

passwords = "Ashley-Madison.txt"
Zip_Path = 'whitehouse_secrets.zip'
progress_every = 10000
    
def load_passwords(path):
    passwords = []
    with open(path, "r") as f:
        for line in f:
            password = line.strip()
            if password:
                passwords.append(password)
    return passwords

def crack(zip_path, passwords):
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for i, password in enumerate(passwords, start=1):
                if i % progress_every == 0:
                    print(f"Trying {i} passwords, currently on: {password}")
                try:
                    zf.extractall(path ="whitehouse_secrets", pwd=password.encode())
                except (RuntimeError, zipfile.BadZipFile, zlib.error):
                        continue
                else:
                        print(f"\nPassword found: {password}")
                        return password
        print("\nNo password in the list worked.")
        return None

if __name__ == "__main__":
    passwords = load_passwords(passwords)
    print(f"Loaded {len(passwords)} candidate passwords from {passwords}")
    crack(Zip_Path, passwords)
        

