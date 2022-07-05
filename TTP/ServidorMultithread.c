//baseado no código fonte de: 
//https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/

//Aluno:/ Hugo Silva de Vasconcelos
//Mat.: 18/0102028

#include <stdio.h>
#include <sys/types.h>
#include <pthread.h>
#include <semaphore.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>


//#define MAX 80
#define PORT 8080
#define SA struct sockaddr

#define FILEIRAS 2    //representa a qtde de fileiras na aeronave
#define ASSENTOS 50   //representa a qtde de assentos por fileira

#define TRUE (0==0)
#define FALSE (0==1)
  
int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;

    int *assentos; //assentos são representados por um vetor unidimensional
    pid_t pid;
    //sem_t mutex;
    int i, j, id_cliente, buff;

    //REGIAO DE MEMORIA COMPARTILHADA PARA OS ASSENTOS
    key_t key1 = ftok("/home/hugo/Downloads/SOR/avaliacao2/server.c",'1');
    int shmid1 = shmget(key1, FILEIRAS*ASSENTOS*sizeof(int), 0644|IPC_CREAT);

    //REGIAO DE MEMORIA COMPARTILHADA PARA O CONTADOR
    key_t key2 = ftok("/home/hugo/Downloads/SOR/avaliacao2/server.c",'2');
    int shmid2 = shmget(key2, sizeof(int), 0644|IPC_CREAT);

    //REGIAO DE MEMORIA COMPARTILHADA PARA O SEMAFORO
    key_t key3 = ftok("/home/hugo/Downloads/SOR/avaliacao2/server.c",'3');
    int shmid3 = shmget(key1, FILEIRAS*ASSENTOS*sizeof(int), 0644|IPC_CREAT);

    printf("chaves de memoria shmid1: %d,shmid2: %d", shmid1, shmid2);
    //pai associa-se a regiao compartilhada
    assentos = shmat(shmid1, (void*)0, 0);
    int *reserv = shmat(shmid2,(void*)0,0);
    int *shmpointer = shmat(shmid3, 0, 0);
    sem_t *mutex = shmpointer;

    if(assentos == (int *)(-1))
        fprintf(stderr,"erro, nao foi possivel associar (shmat)\n");
    //marca assentos livres associando uma valor negativo a estes
    for(int i = 0; i < FILEIRAS*ASSENTOS; i++){
        assentos[i] = -1;
    }
  
    sockfd = socket(AF_INET, SOCK_STREAM, 0); //TCP (vs. UDP)
    if (sockfd == -1) {
        printf("socket falhou...\n");
        exit(1);
    }
    else
        printf("Socket criado com sucesso..\n");
    bzero(&servaddr, sizeof(servaddr));
  
    // atribui IP e PORTA
    memset(&servaddr, '\0', sizeof(servaddr));
    servaddr.sin_family = AF_INET; //IPV4
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    
    // associa socket ao IP e PORTA indicados
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
        printf("socket bind falhou...\n");
        exit(1);
    }
    else
        printf("Socket associado com sucesso..\n");
  
    // prapara servidor para escutar (e configura tamanho da fila para até 100 conexões simultaneas)
    if (listen(sockfd, 10) != 0) {
        printf("Listen falhou...\n");
        exit(1);
    }
    else
        printf("Servidor escutando..\n");
    len = sizeof(cli);
    sem_init(mutex,1,1);
    *reserv = 0;
    while(1){
        // aceita um pedido de conexão do cliente, criando
        // um novo socket "connfd" com o processo cliente
        if(*reserv == (FILEIRAS*ASSENTOS)-1){//Verifica a quantidade de assentos reservados,
            break;                           //caso a quantidade seja igual a quantidade de
                                             // assentos do aviao, interrompe o servidor.
        }
        printf("Aguardando conexão do cliente...\n");
        //connfd = accept(sockfd, (SA*)&cli, &len); 
        if ((connfd = accept(sockfd, (SA*)&cli, &len)) < 0) {
            printf("aceite do servidor falhou...\n");
        }
        else{
            printf("aceite do servidor..\n");
            if((pid = fork()) == 0){ //Cria o processo para lidar com a requisicao
                recv(connfd, &buff, sizeof(int), 0); // recebe o id do cliente
                id_cliente = buff;
                recv(connfd, &buff, sizeof(int), 0); // recebe o id do cliente
                i = buff;
                recv(connfd, &buff, sizeof(int), 0); // recebe o id do cliente
                j = buff;
                sem_wait(mutex); //Entra na regiao critica de memoria pausando o funcionamento dos outros processos
                if(assentos[i*ASSENTOS+j] < 0){ //Caso o assento esteja livre, reserva para o cliente adicionando seu ID na posição escolhida
                    assentos[i*ASSENTOS+j] = id_cliente;
                    buff = 200;
                    printf("[F]:Assento %d/%d reservado para o cliente %d\n", i,j, id_cliente);
                    *reserv += 1;   //Incrementa o contador de assentos reservados
                }else{ //Caso o assento escolhido ja esteja reservado, retorna um erro para o cliente
                    buff = 400;
                    printf("[F]:Requisicao do cliente %d negada, assento %d:%d já está reservado\n", id_cliente, i, j);
                }
                sem_post(mutex);
                send(connfd, &buff, sizeof(int), 0);
                close(connfd);
                printf("[F]:Conexão do cliente %d encerrada\n", id_cliente);
                exit(0);
            }
            printf("processo %d criado..\n", pid);
        }
    }
    
    while(wait(NULL)>0);
    // Termina fechando o socket
    close(sockfd);
    shmdt(assentos);
    shmdt(reserv);
    shmctl(shmid1, IPC_RMID, NULL);
    shmctl(shmid2, IPC_RMID, NULL);
    return 0;
}
