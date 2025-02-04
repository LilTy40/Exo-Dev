#ifndef CARRE_H_INCLUDED
#define CARRE_H_INCLUDED

#include "Couleur.h"
#include "Fenetre.h"


class Carre{
    private:
        int m_x,m_y,m_c;
        Couleur m_couleur;
        void dessiner(Fenetre&,Couleur)const;
    public:
        void placer(int,int);
        int coordX()const;
        int coordY()const;
        void dimensionner(int);
        int cote()const;
        void definirCouleur(int,int,int);
        void definirCouleur(Couleur);
        Couleur couleur()const;
        void afficher(Fenetre&)const;
        void effacer(Fenetre&)const;
        bool touche(int,int)const;
    };


#endif // CARRE_H_INCLUDED
