@echo -off
:Script for config AIC setting of AIM/AIH
:Careat by EFCO Sam
:Version: 1.00
:Date: 2022-05-11

cls
echo "============================================================="
echo "AICCFG.nsh - Program the AIC config by PN select."
echo "ex.AICCFG.nsh 20010-000001"
echo "============================================================="


if %1 == "" then 
  echo "Please input PN number" 
  goto END
endif

cd \AICCFG

if %1 == "10901-000007" then 
 goto AIH
endif

if %1 == "10902-000097" then 
 goto AIM-PI
endif

if %1 == "20010-000160" then 
 goto AIM-PI
endif

if %1 == "20010-000161" then 
 goto AIM-PI
endif

if %1 == "20010-000162" then 
 goto AIM-PI
endif

if %1 == "20010-000170" then 
 goto AIHD
endif

if %1 == "20010-000173" then 
 goto AIML-I
endif

if %1 == "20010-000177" then 
 goto AIML-I
endif

if %1 == "20010-000179" then 
 goto AIML-I
endif

if %1 == "20010-000181" then 
 goto AIHD-I2
endif

if %1 == "20010-000191" then 
 goto AIML-I
endif

if %1 == "20010-000194" then 
 goto AIH
endif

if %1 == "20010-000197" then 
 goto AIH
endif

if %1 == "20010-000199" then 
 goto AIHDP-I
endif

if %1 == "20010-000217" then 
 goto AIMD-2RI
endif

if %1 == "20010-000234" then 
 goto AIHDP
endif

if %1 == "20010-000238" then 
 goto AIML
endif

if %1 == "20010-000249" then 
 goto AIHDP
endif

if %1 == "20010-000263" then 
 goto AIM6RP4I
endif

if %1 == "20010-000287" then 
 goto AIMD-4RI
endif

if %1 == "20010-000303" then 
 goto AIHDP-I
endif

if %1 == "20010-000319" then 
 goto AIM4RP4I
endif

if %1 == "20010-000327" then 
 goto AIM4RP4I
endif

if %1 == "20010-000401" then 
 goto AIM6RP4I
endif

if %1 == "20010-000404" then 
 goto AIML
endif

if %1 == "20010-000407" then 
 goto AIML
endif

if %1 == "999999" then 
 goto DEBUG
endif

echo "%1 PN not find, please check BOM"

goto END

:echo "================================================"
::P=POE, i=ISO-DIO, 6R=RJ45x6
::AICW 
::USB(AIM=4, AIH=6)
::COM(2 or 1)
::POE(8 or 4 or 0)
::DIO(1D=Z, 1I=1, 1D2D=Y, 1I2D=X, 1I2I=2) 
::FAN(AIM=1, AIH=2)

:AIHD
echo "Program AIHD W610Y2" 
W610Y2.nsh
goto END

:AIHDP
echo "Program AIHDP W614Y2" 
W614Y2.nsh
goto END

:AIHD-I2
echo "Program AIHD-I2 W61022" 
W61022.nsh
goto END

:AIHDP-I
echo "Program AIHDP-I W614X2" 
W614X2.nsh
goto END

:AIHDP-I2
echo "Program AIHDP-I2 W61422" 
W61422.nsh
goto END

:AIH-I
echo "Program AIH-I W62812" 
W62812.nsh
goto END

:AIH
echo "Program AIH W628Z2" 
W628Z2.nsh
goto END

:AIML
echo "Program AIML W410Z1" 
W410Z1.nsh
goto END

:AIML-I
echo "Program AIML-I W41011" 
W41011.nsh
goto END

:AIM-PI
echo "Program AIM-PI W42411" 
W42411.nsh
goto END

:AIMD-2RI
echo "Program AIMD-2RI W41011" 
W41011.nsh
goto END

:AIMD-4RI
echo "Program AIMD-4RI W41011" 
W41011.nsh
goto END

:AIM4RP4I
echo "Program AIM4RP4I W41411" 
W41411.nsh
goto END

:AIM6RP4I
echo "Program AIM6RP4I W41411" 
W41411.nsh
goto END



:DEBUG
echo "DEBUG"
echo "Program AIH-I W62812" 
W62812.nsh
goto END

:END
cd \
:cd uefi
echo "command ststus: %lasterror% "
if %lasterror% == 0 then
    echo "Update Done"
else
    echo "Update Fail"
endif




