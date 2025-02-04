#include "bouton.h"

void Bouton::definir(int x, int y, int t, int r, int v, int b, bool etat){
    (*this).m_c.placer(x,y);
    (*this).m_c.dimensionner(t);
    (*this).m_c.definirCouleur(r,v,b);
    (*this).m_estActif = etat;
}
void Bouton::activer(){
    (*this).m_estActif = true;
}

bool Bouton::actif() const{
    return (*this).m_estActif;
}

int Bouton::coordX() const{
    return (*this).m_c.coordX();
}

void Bouton::afficher(Fenetre& f) const{
    (*this).m_c.afficher(f);

    if ((*this).m_estActif)
    {
        f.remplitEllipse((*this).coordX()-(*this).rayon()/2,(*this).coordY()-(*this).rayon()/2,(*this).rayon(),(*this).rayon());
    }   
}

void Bouton::effacer(Fenetre& f) const{
    (*this).m_c.effacer(f);

    if ((*this).m_estActif)
    {
        f.remplitEllipse((*this).coordX()-(*this).rayon()/2,(*this).coordY()-(*this).rayon()/2,(*this).rayon(),(*this).rayon());
    }   
}

bool Bouton::touche(int x, int y) const{
    return (*this).m_c.touche(x,y);
}
