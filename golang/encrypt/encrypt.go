package encrypt

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/hex"
	"os"
)

// Encrypt will encrypt a raw string to
// an encrypted value
// an encrypted value has an IV (nonce) + actual encrypted value
// when we decrypt, we only decrypt the latter part
func Encrypt(key []byte) ([]byte, error) {
	secretKey := getSecret()

	block, err := aes.NewCipher(secretKey)
	if err != nil {
		return nil, err
	}

	aesgcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}

	iv := make([]byte, aesgcm.NonceSize())
	if _, err := rand.Read(iv); err != nil {
		return nil, err
	}

	ciphertext := aesgcm.Seal(iv, iv, key, nil)

	return ciphertext, nil
}

func getSecret() []byte {
	// for simplicity, the master key will be stored as an environment variable.
	secret := os.Getenv("SECRET")
	if secret == "" {
		panic("Error: Must provide a secret key under env variable SECRET")
	}

	secretbite, err := hex.DecodeString(secret)

	if err != nil {
		// probably malform secret, panic out
		panic(err)
	}
	return secretbite
}
