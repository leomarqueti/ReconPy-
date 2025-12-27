# ReconPy

ReconPy é uma ferramenta simples de **OSINT (Open Source Intelligence)** desenvolvida em **Python**, com foco em **automação de reconhecimento (recon)** para estudos em Pentest.

O projeto foi criado como aplicação prática após a conclusão do módulo de Python dentro da trilha de Pentest da **Solyd**, com o objetivo de sair do conteúdo básico do curso e aplicar o aprendizado em um projeto real.

---
<img width="1111" height="618" alt="image" src="https://github.com/user-attachments/assets/6026096f-b9e9-4c2b-90c2-17de500696a6" />

## 🎯 Objetivo do Projeto

- Praticar consumo de APIs públicas
- Trabalhar com respostas HTTP reais (200, 403, 404)
- Tratar erros e respostas inesperadas
- Organizar um pequeno projeto em Python
- Criar uma interface amigável no terminal
- Conectar Python com o contexto de Pentest / OSINT

---

## 🚀 Funcionalidades

### 🔍 IP Lookup
Consulta informações de um endereço IP, como:
- País
- Cidade
- Região
- Provedor / ASN

Utiliza API pública para obtenção dos dados.

<img width="1116" height="618" alt="image" src="https://github.com/user-attachments/assets/a0ca1d7c-4e77-4c22-b413-2660b3484741" />


---

### 👤 Username Recon
Verifica a existência de usernames em diferentes plataformas:
- GitHub
- Reddit

Quando disponível, exibe informações públicas do perfil.

<img width="1109" height="621" alt="image" src="https://github.com/user-attachments/assets/4d142738-2569-4f2d-bd9d-e2a94df6ed29" />


---

## 🛠️ Tecnologias Utilizadas

- Python 3
- requests
- rich

---

## ⚠️ Observações Importantes

- Algumas plataformas podem aplicar bloqueios (ex: HTTP 403), o que é tratado pela aplicação.
- O projeto não tenta burlar proteções nem realizar scraping agressivo.
- Ferramenta desenvolvida **exclusivamente para fins educacionais**.

---

## 📚 Contexto de Aprendizado

Este projeto faz parte do meu processo de estudo em:
- Python
- Pentest
- OSINT
- Automação de tarefas

Ainda é um projeto em evolução, focado em aprendizado e prática.

---

## 📌 Próximos Passos (Ideias)

- Padronizar retornos das funções
- Organizar o projeto em múltiplos arquivos
- Adicionar novas plataformas de username recon
- Exportar resultados para arquivo

---

## 👤 Autor

Desenvolvido por **Leonardo Marqueti**  
Estudante de Python e Pentest
