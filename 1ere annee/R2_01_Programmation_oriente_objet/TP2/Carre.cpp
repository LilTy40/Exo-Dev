#include "Couleur.h"
#include "Fenetre.h"
#include "Souris.h"
#include "Carre.h"

void Carre::dessiner(Fenetre& f,Couleur c)const
{
    f.choixCouleurTrace(c);
    f.traceLigne(m_x,m_y,m_x+m_c,m_y);
    f.traceLigne(m_x+m_c,m_y,m_x+m_c, m_y+m_c);
    f.traceLigne(m_x+m_c,m_y+m_c,m_x, m_y+m_c);
    f.traceLigne(m_x, m_y+m_c,m_x,m_y);
}

void Carre::placer(int x,int y)
{
    (*this).m_x = x;
    (*this).m_y = y;
}

int Carre::coordX()const
{
    return(*this).m_x;
}

int Carre::coordY()const
{
    return(*this).m_y;
}

void Carre::dimensionner(int cote)
{
    (*this).m_c = cote;
}

int Carre::cote()const
{
    return(*this).m_c;
}

void Carre::definirCouleur(int r,int g,int b)
{
    (*this).m_couleur.definir(r,g,b);
}

void Carre::definirCouleur(Couleur c)
{
    (*this).m_couleur.definir(c.rouge(),c.vert(),c.bleu());
}

Couleur Carre::couleur()const
{
    return(*this).m_couleur;
}

void  Carre::afficher(Fenetre& f)const
{
    (*this).dessiner(f,(*this).m_couleur);
}

void Carre::effacer(Fenetre& f)const
{
    (*this).dessiner(f,f.couleurFond());
}

bool Carre::touche(int x,int y) const
{
    return((*this).m_x<=x&&(*this).m_x + (*this).m_c>=x &&(*this).m_y<=y&&(*this).m_y+(*this).m_c>=y);
}
