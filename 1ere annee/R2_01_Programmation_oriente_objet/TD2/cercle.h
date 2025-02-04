#ifndef _CERCLE_H
#define _CERCLE_H

#include "Fenetre.h"
#include "Couleur.h"

class Cercle{
    protected:
        int m_x;
        int m_y;
        int m_r;
        Couleur m_coul;

    public:
        void placer(int, int);
        void dimensionner(int);
        void definirCouleur(int, int, int);
        void definirCouleur(Couleur);
        int coordX() const;
        int coordY() const;
        int rayon() const;
        Couleur couleur() const;
        void afficher(Fenetre&) const;
        void effacer(Fenetre&) const;
        bool touche(int, int) const;

};

#endif