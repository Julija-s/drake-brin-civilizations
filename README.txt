


najprej uredimo okolje:

    $env:CIV_USE_TEX="1"                                                 
    >> $env:CIV_SAVE_PDF="1"

generiranje podatkov za osnovne in supermodele: 

    python main.py clean generate plot super 

če hočemo samo osnovne:

    python main.py clean generate plot

importance grid: 

    python importance_grid.py --out outputs --dist lognormal --super-dist mixed  

pca analiza:

    python main.py pca


osnovni + supermodeli + pca:

    python main.py clean generate plot super pca

za izris slikice ki kaže ratlike distribucij samo zaženemo: distributions.py


