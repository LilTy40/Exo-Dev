#ifndef _BOUTON_H
#define _BOUTON_H

//#include "Fenetre.h"
#include "Couleur.h"
#include "cercle.h"

class bouton
{
protected:
    Cercle m_c;
    bool m_estActif;
public:
    void definir(int, int, int, int, int, int, bool = false);
    void definir(int, int, int, Couleur = Couleur(0,0,255), bool = false);
    void activer();
    void desactiver();
    bool actif() const;
    int coordX() const;
    int coordY() const;
    int rayon() const;
    void definirCouleur(Couleur);
    Couleur couleur() const;
    void afficher(Fenetre&) const;
    void effacer(Fenetre&) const;
    bool touche(int, int) const;
};

#endif

