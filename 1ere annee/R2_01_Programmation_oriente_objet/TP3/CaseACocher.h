#ifndef CASEACOCHER_H
#define CASEACOCHER_H

#include "Carre.h"

class CaseACocher{

    protected:
        Carre m_carre;
        bool m_estCoche

    public:
        void definirCadre(int, int, int, Couleur couleur);
        Carre cadre() const;
        void definirEtat(char);
        char etat() const;
        void afficher(Fenetre&) const;
        void effacer(Fenetre&) const;
}

#endif // CASEACOCHER_H
