package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"errors"
	"fmt"
)

var key_text = "astaxie12798akljzmknm.ahkjkljl;k"
var key_text_front = "se2axie62793akljzm34m.ahkjk5jl;f"
var commonIV = []byte{0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f}

//EncryptAES
func EncryptAES(text string, key string) (string, error) {
	//aes的加密字符串

	c, err := aes.NewCipher([]byte(key))
	if err != nil {
		return "", errors.New(fmt.Sprintf("Error: NewCipher(%d bytes) = %s", len(key), err))
	}

	//加密字符串
	cfb := cipher.NewCFBEncrypter(c, commonIV)
	ciphertext := make([]byte, len(text))
	cfb.XORKeyStream(ciphertext, []byte(text))
	return string(ciphertext), nil
}

func base64Encode(src []byte) []byte {
	return []byte(base64.StdEncoding.EncodeToString(src))
}

func base64Decode(src []byte) ([]byte, error) {
	return base64.StdEncoding.DecodeString(string(src))
}

func EncryptPassword(ticket string) (string, error) {

	encodeStr, err := EncryptAES(ticket, key_text_front)
	if err != nil {
		return "", err
	}
	encode := base64Encode([]byte(encodeStr))
	if err != nil {
		return "", err
	}

	return string(encode), nil
}

func main() {
	//if len(os.Args) != 2 {
	//	fmt.Printf("usage ./encrypt_password DecodePassword \n")
	//	return
	//}
	//input := os.Args[1]
	input := "1qaz!QAZ"
	encode, _ := EncryptPassword(input)
	fmt.Printf("decode password result [%s]\n", encode)

}