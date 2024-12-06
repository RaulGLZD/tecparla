#! /usr/bin/bash

NOM=UNO

DIR_WRK=$PWD

DIR_LOG=$DIR_WRK/Log
FIC_LOG=$DIR_LOG/$(basename $0 .sh).$NOM.log
[ -d $DIR_LOG ] || mkdir -p $DIR_LOG

exec > >(tee $FIC_LOG) 2>&1

hostname
pwd
date

PRM=true
ENT=true
REC=true
EVA=true

DIR_GUI=$DIR_WRK/Gui
GUI_ENT=$DIR_GUI/train.gui
GUI_DEV=$DIR_GUI/devel.gui

DIR_SEN=$DIR_WRK/Sen
DIR_PRM=$DIR_WRK/Prm/$NOM
DIR_REC=$DIR_WRK/Rec/$NOM

FIC_MOD=$DIR_WRK/Mod/$NOM.mod
[ -d $(dirname $FIC_MOD) ] || mkdir -p $(dirname $FIC_MOD )

LIST_MOD=$DIR_WRK/Lis/vocales.lis

FIC_RES=$DIR_WRK/Res/$NOM.res
[ -d $(dirname $FIC_RES) ] || mkdir -p $(dirname $FIC_RES )

EXEC="parametriza.py -p $DIR_PRM -s $DIR_SEN $GUI_ENT $GUI_DEV"
$PRM && echo $EXEC && $EXEC || exit 1

dirPrm="-p $DIR_PRM"
dirMar="-m $DIR_SEN"
ficMod="-f $FIC_MOD"
listMod="-l $LIST_MOD"

EXEC="entrena.py $dirPrm $dirMar $ficMod $listMod $GUI_ENT"
$ENT && echo $EXEC && $EXEC || exit 1

ficMod="-f $FIC_MOD"
dirRec="-r $DIR_REC"
dirPrm="-p $DIR_PRM"

EXEC="reconoce.py $dirPrm $dirRec $ficMod $GUI_DEV"
$REC && echo $EXEC && $EXEC || exit 1

dirRec="-r $DIR_REC"
dirMar="-m $DIR_SEN"


EXEC="evalua.py $dirMar $dirRec $GUI_DEV"
$EVA && echo $EXEC && $EXEC | tee $FIC_RES|| exit 1
