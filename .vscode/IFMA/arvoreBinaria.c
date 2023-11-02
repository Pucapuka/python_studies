#include <stdio.h>
#include <stdlib.h>

typedef struct SArvore{
    struct SArvore * esq;
    int dado;
    struct SArvore * dir;
}TArvore;

//Sentinela
TArvore *raiz;


void preOrdem(TArvore *no){
    if (no==NULL) return;
    printf("%d", no->dado);
    preOrdem(no->esq);
    preOrdem(no->dir);

}

void Ordem(TArvore *no){
    if (no==NULL) return;
    preOrdem(no->esq);
    printf("%d", no->dado);
    preOrdem(no->dir);

}

void posOrdem(TArvore *no){
    if (no==NULL) return;
    preOrdem(no->esq);
    preOrdem(no->dir);
    printf("%d", no->dado);

}



int main(){

    raiz = malloc(sizeof(TArvore));
    raiz->dado = 1;
    raiz->esq = raiz->dir = NULL; //só tem a raiz, por isso são nulos

    //usando variável auxiliar
    TArvore *filho = malloc(sizeof(TArvore));
    filho->dado = 2;
    filho->esq = filho->dir = NULL;
    raiz->esq = filho;

    //usando a própria raiz
    raiz->dir = malloc(sizeof(TArvore));
    raiz->dir->dado = 3;
    raiz->dir->esq = raiz->dir->dir = NULL;

    filho = malloc(sizeof(TArvore));
    filho->dado = 4;
    filho->esq = filho->dir = NULL;
    raiz->esq->esq = filho;

    filho = malloc(sizeof(TArvore));
    filho->dado = 5;
    filho->esq = filho->dir = NULL;
    raiz->esq->dir = filho;

    filho = malloc(sizeof(TArvore));
    filho->dado = 6;
    filho->esq = filho->dir = NULL;
    raiz->dir->esq = filho;

    filho = malloc(sizeof(TArvore));
    filho->dado = 7;
    filho->esq = filho->dir = NULL;
    raiz->dir->dir = filho;

    printf("Pré-ordem\n");
    preOrdem(raiz);
    
    return 0;
}