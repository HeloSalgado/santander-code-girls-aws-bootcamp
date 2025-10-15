# Criando primeiro bucket no S3

Estudo em: October 7, 2025 5:59 PM

![image.png](image.png)

![image.png](image%201.png)

![image.png](image%202.png)

![image.png](image%203.png)

## Pastas do bucket

![image.png](image%204.png)

## Dando permissão para o bucket ficar público

![image.png](image%205.png)

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "PublicReadGetObject",
			"Principal": "*",
			"Effect": "Allow",
			"Action": [
				"s3:GetObject"
			],
			"Resource": "arn:aws:s3:::desafioawsantander/*" // seu bucket arn - /* da acesso a tudo dentro do bucket
		}
	]
}
```

## Logo depois criar um ponto de acesso

![image.png](image%206.png)