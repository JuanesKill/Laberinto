conecta(inicio,8).
conecta(47,fin).
conecta(1, 2).
conecta(1, 7).
conecta(2, 3).
conecta(2, 8).
conecta(3, 9).
conecta(7, 8).
conecta(7, 13).
conecta(8, 9).
conecta(8,14).
conecta(9,15).
conecta(13,14).
conecta(13,19).
conecta(14,20).
conecta(14,15).
conecta(19,20).
conecta(19,25).
conecta(20,21).
conecta(25,28).
conecta(28,34).
conecta(34,35).
conecta(34,38).
conecta(38,42).
conecta(42,43).
conecta(43,44).
conecta(44,45).
conecta(45,39).
conecta(45,46).
conecta(39,40).
conecta(40,46).
conecta(46,47).
conecta(40,41).
conecta(41,47).
conecta(41,37).
conecta(35,29).
conecta(35,36).
conecta(29,30).
conecta(30,36).
conecta(30,31).
conecta(31,32).
conecta(32,33).
conecta(33,37).
conecta(26,32).
conecta(27,33).
conecta(26,27).
conecta(26,23).
conecta(27,24).
conecta(23,24).
conecta(22,23).
conecta(22,16).
conecta(23,17).
conecta(24,18).
conecta(16,10).
conecta(16,17).
conecta(17,11).
conecta(17,18).
conecta(18,12).
conecta(10,11).
conecta(10,4).
conecta(11,5).
conecta(11,12).
conecta(12,6).
conecta(4,5).
conecta(5,6).
conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).
conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).
miembro(X,[X|_]).
miembro(X,[_|Y]) :- miembro(X,Y).
sol :- camino([inicio],Sol),write(Sol).
camino([fin|RestoDelCamino],[fin|RestoDelCamino]).
camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino),camino([PosSiguiente,PosActual|RestoDelCamino],Sol).
