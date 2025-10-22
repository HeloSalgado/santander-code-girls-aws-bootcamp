# Amazon S3

Estudo em: October 21, 2025

O Amazon S3 é um serviços de armazenamento de objetos em nuvem oferecidos pela AWS. Ele é ideal para armazenar, organizar e recuperar grandes volumes de dados de forma segura e escalável.

## Características

- Armazenamento de Objetos: Cada objeto é armazenado em um bucket.
- Buckets: São contêineres para objetos que podemos armazenar no S3. Cada buckettem um nome globalmente único.
- Possui Classes de Armazenamento: O S3 tem diferentes classes de armazenamento para otimizar custos e o desempenho. Possui o S3 Standard, S3 Intelligent-Tiering, S3 Glacier, entre outras classes.
- Durabilidade e garantia: Foi projetado para fornecer 99,999999999% de durabilidade e 99,99% de disponibilidade dos objetos.
- Segurança: Criptografia de dados em repouso e em trânsito, controle de acesso granularusando políticas e a lista de Controle de Acesso.

## Políticas de Acesso

Com as políticas do Amazon S3 podemos proteger o acesso aos objetos dos buckets e com isso conseguimos criar regras de acesso exclusivas.Isso reduz o risco de exposição indesejada e permite que apenas entidades autorizadas acessem os dados.

Através do IAM (AWS Identity and Access Management), conseguimos criar a nossa política de acesso aos nossos buckets.

Através de um Json com chave e valor, conseguimos definir os nossos acessos.

Política de Bucket para Tornar o Bucket Público:

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