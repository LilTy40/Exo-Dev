#include "CaseACocher.h"
#include "Fenetre.h"
#include "Couleur.h"
#include "Carre.h"

void CaseACocher::definirCadre(int x, int y, int longueur, Couleur couleur){
    (*this).m_carre.placer(x,y);
    (*this).m_carre.dimensionner(longueur);
    (*this).m_carre.definirCouleur(couleur)
};

Carre CaseACocher::cadre() const{
    return (*this).m_carre
}

void CaseACocher::definirEtat(char etat){

    if(etat == 'C'){
        (*this).m_estCoche = true;
    }
    else if(etat == 'N'){
        (*this).m_estCoche = false
    }
}

char CaseACocher::etat() const{
    if (*this).m_estCoche == true){
        return 'C'
    }
    else{
        return 'N'
    }
}
