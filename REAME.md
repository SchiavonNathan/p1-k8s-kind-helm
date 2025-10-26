# p1 Helm Chart

O projeto consiste em:
1.  Uma aplicação web simples em **Python/Flask**.
2.  Um **Dockerfile** para containerizar a aplicação.
3.  Um **Helm Chart** customizado para fazer o deploy da aplicação no Kubernetes.

## Tecnologias Utilizadas

* Python (Flask)
* Docker
* Kubernetes (testado com `kind`)
* Helm

## Como Executar Localmente

1.  **Pré-requisitos:**
    * `docker`
    * `kind`
    * `helm`
    * `kubectl`

2.  **Construa a imagem Docker:**
    ```bash
    cd app/
    docker build -t meu-app-helm:v1.0.0 .
    ```

3.  **Crie um cluster `kind` e carregue a imagem:**
    ```bash
    kind create cluster
    kind load docker-image meu-app-helm:v1.0.0
    ```

4.  **Instale o Helm Chart:**
    (A partir da raiz do projeto)
    ```bash
    helm install meu-release ./meu-chart
    ```

5.  **Acesse a aplicação:**
    ```bash
    kubectl port-forward svc/meu-release-meu-chart 8080:5000
    ```
    Abra `http://localhost:8080` no seu navegador.

6.  **Limpeza:**
    ```bash
    helm uninstall meu-release
    kind delete cluster
    ```
