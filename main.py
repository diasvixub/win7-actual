from os import system, listdir, getcwd
from time import sleep
from subprocess import run, DEVNULL
import sys
from datetime import *
from elevate import elevate

hr = '═══════════════════════════════════════════════════════════════════════════════'
dism_list = ['/FeatureName:WindowsGadgetPlatform ', '/FeatureName:InboxGames', '/FeatureName:More Games',
             '/FeatureName:Solitaire', '/FeatureName:SpiderSolitaire', '/FeatureName:Hearts', '/FeatureName:FreeCell',
             '/FeatureName:Minesweeper', '/FeatureName:PurplePlace']
sc_list = ['WSearch', 'SDRSVC', 'TabletInputService', 'bthserv', 'BDESVC', 'VSS', 'SCardSvr', 'WinDefend']


f = open(f'logs\\{date.today()}.log', 'w', encoding='utf-8')
f.write(f'Program start [{datetime.now()}] \n')
f.write(f'{hr} \n')


def main():
    system('cls')
    system('title MENU # WIN7-ACTUAL')
    print('Select the desired action')
    print(hr)
    print('1 System Russification')
    print('2 Installing updates')
    print('3 Root certificates update')
    print('4 Installing libraries')
    print('5 Installing programs')
    print('6 Windows optimization')
    print('7 Temporary files cleaning')
    print('8 Getting help')
    print('0 Exit')
    print(hr)
    action = input('Operation number: ')
    if action == '1':
        f.write(f'Go to the "System Russification" section [{datetime.now()}] \n')
        ru()
    elif action == '2':
        f.write(f'Go to the "Installing updates" section [{datetime.now()}] \n')
        updates()
    elif action == '3':
        f.write(f'Go to the "Root certificates update" section [{datetime.now()}] \n')
        certs()
    elif action == '4':
        f.write(f'Go to the "Installing libraries" section [{datetime.now()}] \n')
        libs()
    elif action == '5':
        f.write(f'Go to the "Installing programs" section [{datetime.now()}] \n')
        programs()
    elif action == '6':
        f.write(f'Go to the "Windows optimization" section [{datetime.now()}] \n')
        boost(dism_list, sc_list)
    elif action == '7':
        f.write(f'Go to the "Temporary files cleaning" section [{datetime.now()}] \n')
        clean()
    elif action == '8':
        f.write(f'Using help [{datetime.now()}] \n')
        system('start readme.html')
        main()
    elif action == '0':
        f.write(f'Exiting the program [{datetime.now()}] \n')
        f.close()
        sys.exit()
    else:
        f.write(f'Invalid operation number entered: {action} [{datetime.now()}] \n')
        print('Invalid operation number entered')
        sleep(1)
        f.write(f'Go to Menu [{datetime.now()}] \n')
        main()


def ru():
    try:
        system('title RUSSIFICATION # WIN7-ACTUAL')
        system('cls')
        try:
            run('ru\\kb2483139.exe', shell=True, stdout=DEVNULL)
        except FileNotFoundError:
            f.write(f'except FileNotFoundError. Go to Menu [{datetime.now()}] \n')
            print('File not found')
            sleep(1)
            main()
        else:
            cwd = getcwd()
            f.write(f'Installation of Russian localization... [{datetime.now()}] \n')
            run(f'DISM /Online /Add-Package /PackagePath:"{cwd}\\lp.cab"', shell=True, stdout=DEVNULL)
            system('bcdedit /set {current} locale ru-RU')
            system('bcdboot %WinDir% /l ru-RU')
            run(['reg', 'delete', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\MUI\\UILanguages\\en-US', '/f'],
                shell=True, stdout=DEVNULL)
            f.write(f'Installation of Russian localization was successful [{datetime.now()}] \n')
            while True:
                system('cls')
                print('''
The installation of the Russian language was successful.
To apply the changes, you need to restart your computer.
Continue?''')
                print(hr)
                action = input('Yes/No [Y/N]: ')
                action.lower()
                if action == 'yes' or action == 'y':
                    f.write(f'Reboot system [{datetime.now()}] \n')
                    f.close()
                    run(['shutdown', '/r', '/t', '0'], shell=True, stdout=DEVNULL)
                    sys.exit()
                elif action == 'no' or action == 'n':
                    f.write(f'Go to Menu [{datetime.now()}] \n')
                    main()
                else:
                    f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                    system('cls')
                    print('Invalid param entered')
                    sleep(1)
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


def updates():
    try:
        system('title UPDATES # WIN7-ACTUAL')
        system('cls')
        print('Select the desired action')
        print(hr)
        print('1 Updating the Windows Update Agent')
        print('2 Installing Windows updates')
        print('0 Go to main menu')
        print(hr)
        action = input('Operation number: ')
        if action == '1':
            f.write(f'Change "Updating the Windows Update Agent" [{datetime.now()}] \n')
            system('cls')
            print('Updating the Windows Update Agent...')
            run('agent\\windowsupdateagent-7.6-x64.exe', shell=False, stdout=DEVNULL)
            f.write(f'The Windows Update Agent update was successful" [{datetime.now()}] \n')
            while True:
                system('cls')
                print('''
The Windows Update Agent update was successful.
To apply the changes, you need to restart your computer.
Continue?''')
                print(hr)
                action = input('Yes/No [Y/N]: ')
                action.lower()
                if action == 'yes' or action == 'y':
                    f.write(f'Reboot system [{datetime.now()}] \n')
                    f.close()
                    run(['shutdown', '/r', '/t', '0'], shell=True, stdout=DEVNULL)
                    sys.exit()
                elif action == 'no' or action == 'n':
                    f.write(f'Go back in Updates menu" [{datetime.now()}] \n')
                    updates()
                else:
                    f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                    system('cls')
                    print('Invalid param entered')
                    sleep(1)
        elif action == '2':
            f.write(f'Change "Installing Windows updates" [{datetime.now()}] \n')
            system('cls')
            updates_list = listdir('updates')
            if len(updates_list) == 0:
                f.write(f'No updates found [{datetime.now()}] \n')
                print('''
No updates found.
Put the update files in the "updates" folder and try again.''')
                print(hr)
                input('Continue...')
                f.write(f'Go to Updates [{datetime.now()}] \n')
                updates()
            else:
                f.write(f'{len(updates_list)} updates will be installed [{datetime.now()}] \n')
                while True:
                    print(f'{len(updates_list)} updates will be installed. Continue?')
                    print(hr)
                    action = input('Yes/No [Y/N]: ')
                    action.lower()
                    if action == 'yes' or action == 'y':
                        system('cls')
                        for i in updates_list:
                            f.write(f'Installation {i}... [{datetime.now()}] \n')
                            print(f'Installation {i}...')
                            run(f'wusa.exe updates\\{i} /quiet /norestart', shell=False, stdout=DEVNULL)
                            system('cls')
                        f.write(f'The Windows Updates install was successful [{datetime.now()}] \n')
                        while True:
                            system('cls')
                            print('''
The Windows Updates install was successful.
To apply the changes, you need to restart your computer.
Continue?''')
                            print(hr)
                            action = input('Yes/No [Y/N]: ')
                            action.lower()
                            if action == 'yes' or action == 'y':
                                f.write(f'Reboot system [{datetime.now()}] \n')
                                f.close()
                                run(['shutdown', '/r', '/t', '0'], shell=True, stdout=DEVNULL)
                                sys.exit()
                            elif action == 'no' or action == 'n':
                                f.write(f'Go to Menu [{datetime.now()}] \n')
                                main()
                            else:
                                f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                                system('cls')
                                print('Invalid param entered')
                                sleep(1)
                    elif action == 'no' or action == 'n':
                        f.write(f'Go to Menu [{datetime.now()}] \n')
                        main()
                    else:
                        f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                        system('cls')
                        print('Invalid param entered')
                        sleep(1)
        elif action == '0':
            f.write(f'Go to Menu [{datetime.now()}] \n')
            main()
        else:
            f.write(f'Invalid param entered: {action} [{datetime.now()}] \n')
            system('cls')
            print('Invalid param entered')
            sleep(1)
            f.write(f'Go to Updates [{datetime.now()}] \n')
            updates()
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()
    except FileNotFoundError:
        f.write(f'except FileNotFoundError. Go to Menu [{datetime.now()}] \n')
        print('The "updates" directory was not found')
        sleep(1)
        main()


def certs():
    try:
        f.write(f'Certificate update... [{datetime.now()}] \n')
        system('title CERTS # WIN7-ACTUAL')
        system('cls')
        print('Click "No" in the windows that appear on the screen')
        system('certs\\rootsupd.exe /c /t:%CD%\\certs\\')
        system('certs\\updroots.exe certs\\roots.sst')
        system('cls')
        f.write(f'Certificate update completed successfully [{datetime.now()}] \n')
        print('Certificate update completed successfully')
        sleep(1)
        f.write(f'Go to Menu [{datetime.now()}] \n')
        main()
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


def libs():
    try:
        system('title LIBS # WIN7-ACTUAL')
        system('cls')
        libs_list = listdir('libs')
        if len(libs_list) == 0:
            f.write(f'No libs found [{datetime.now()}] \n')
            print('''
No libs found.
Put the update files in the "libs" folder and try again.''')
            print(hr)
            input('Continue...')
            f.write(f'Go to Libs [{datetime.now()}] \n')
            libs()
        else:
            f.write(f'{len(libs_list)} libs will be installed [{datetime.now()}] \n')
            while True:
                print(f'{len(libs_list)} libs will be installed. Continue?')
                print(hr)
                action = input('Yes/No [Y/N]: ')
                action.lower()
                if action == 'yes' or action == 'y':
                    system('cls')
                    for i in libs_list:
                        f.write(f'Installation {i}... [{datetime.now()}] \n')
                        print(f'Installation {i}...')
                        run(f'libs\\{i}', shell=False, stdout=DEVNULL)
                        system('cls')
                    print('The libs install was successful.')
                    sleep(1)
                    f.write(f'Go to Menu [{datetime.now()}] \n')
                    main()
                elif action == 'no' or action == 'n':
                    f.write(f'Go to Menu [{datetime.now()}] \n')
                    main()
                else:
                    f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                    system('cls')
                    print('Invalid param entered')
                    sleep(1)
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


def programs():
    try:
        system('title PROGRAMS # WIN7-ACTUAL')
        system('cls')
        programs_list = listdir('programs')
        if len(programs_list) == 0:
            f.write(f'No programs found [{datetime.now()}] \n')
            print('''
No programs found.
Put the update files in the "programs" folder and try again.''')
            print(hr)
            input('Continue...')
            programs()
        else:
            f.write(f'{len(programs_list)} libs will be installed [{datetime.now()}] \n')
            while True:
                print(f'{len(programs_list)} libs will be installed. Continue?')
                print(hr)
                action = input('Yes/No [Y/N]: ')
                action.lower()
                if action == 'yes' or action == 'y':
                    system('cls')
                    for i in programs_list:
                        f.write(f'Installation {i}... [{datetime.now()}] \n')
                        print(f'Installation {i}...')
                        run(f'{i}', shell=False, stdout=DEVNULL)
                        system('cls')
                    print('The libs install was successful.')
                    sleep(1)
                    f.write(f'Go to Menu [{datetime.now()}] \n')
                    main()
                elif action == 'no' or action == 'n':
                    f.write(f'Go to Menu [{datetime.now()}] \n')
                    main()
                else:
                    f.write(f'Invalid param entered in action yes/no: {action} [{datetime.now()}] \n')
                    system('cls')
                    print('Invalid param entered')
                    sleep(1)
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


def boost(a, b):
    try:
        system('title OPTIMIZATION # WIN7-ACTUAL')
        system('cls')
        f.write(f'Disabling Windows components... [{datetime.now()}] \n')
        print('Disabling Windows components...')
        for i in a:
            f.write(f'Disabling {i}... [{datetime.now()}] \n')
            run(f'Dism /online /Disable-Feature {i} /norestart', shell=False, stdout=DEVNULL)
        system('cls')
        f.write(f'Configuring the Swap file... [{datetime.now()}] \n')
        print('Configuring the Swap file')
        f.write(f'Disabling automatic selection of the swap file size... [{datetime.now()}] \n')
        run('wmic computersystem set AutomaticManagedPagefile=False', shell=False, stdout=DEVNULL)
        print(hr)
        while True:
            try:
                action = int(input('Enter the amount of RAM (GB): '))
            except ValueError:
                f.write(f'except ValueError [{datetime.now()}] \n')
                system('cls')
                print('Enter a number')
                sleep(1)
                system('cls')
            else:
                f.write(f'Input {action} GB RAM [{datetime.now()}] \n')
                if 0 < action <= 8:
                    f.write(f'Setting the swap file size: 4 GB... [{datetime.now()}] \n')
                    run('wmic pagefileset where name="C:\\\\pagefile.sys" set InitialSize=4096,MaximumSize=4096',
                        shell=False, stdout=DEVNULL)
                    break
                elif 8 < action <= 16:
                    f.write(f'Setting the swap file size: 2 GB... [{datetime.now()}] \n')
                    run('wmic pagefileset where name="C:\\\\pagefile.sys" set InitialSize=2048,MaximumSize=2048',
                        shell=False, stdout=DEVNULL)
                    break
                elif action > 16:
                    f.write(f'Setting the swap file size: 1 GB... [{datetime.now()}] \n')
                    run('wmic pagefileset where name="C:\\\\pagefile.sys" set InitialSize=1024,MaximumSize=1024',
                        shell=False, stdout=DEVNULL)
                    break
                elif action <= 0:
                    f.write(f'Invalid RAM value entered: {action} [{datetime.now()}] \n')
                    print('The amount of memory cannot be 0 or less')
                    sleep(1)
                    continue
                else:
                    pass
        system('cls')
        f.write(f'Enabling the display of file extensions... [{datetime.now()}] \n')
        print('Enabling the display of file extensions...')
        run('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v HideFileExt /t REG_DWORD /d 00000000 /f',
            shell=False, stdout=DEVNULL)
        system('cls')
        f.write(f'Disabling services... [{datetime.now()}] \n')
        for i in b:
            f.write(f'Disabling {i}... [{datetime.now()}] \n')
            print('Disabling services...')
            run(f'sc config {i} start= disabled', shell=False, stdout=DEVNULL)
            system('cls')
        f.write(f'Optimization was successful [{datetime.now()}] \n')
        print('Optimization was successful')
        sleep(1)
        f.write(f'Go to Menu [{datetime.now()}] \n')
        main()
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


def clean():
    try:
        system('title CLEAN # WIN7-ACTUAL')
        system('cls')
        f.write(f'Temporary files cleaning... [{datetime.now()}] \n')
        print('Temporary files cleaning...')
        system('del C:\\Windows\\SoftwareDistribution\\Download\\*.* /s /q >nul 2>&1')
        system('for /d %i in (C:\\Windows\\SoftwareDistribution\\Download\\*.*) do @rmdir /s /q "%i" >nul 2>&1',)
        system('del C:\\Windows\\Prefetch\\*.* /s /q >nul 2>&1')
        system('for /d %i in (C:\\Windows\\Prefetch\\*.*) do @rmdir /s /q "%i" >nul 2>&1')
        system('del %temp%\\*.* /s /q >nul 2>&1')
        system('for /d %i in (%temp%\\*.*) do @rmdir /s /q "%i" >nul 2>&1')
        system('cls')
        f.write(f'Cleaning was successful [{datetime.now()}] \n')
        print('Cleaning was successful')
        sleep(1)
        f.write(f'Go to Menu [{datetime.now()}] \n')
        main()
    except KeyboardInterrupt:
        f.write(f'except KeyboardInterrupt. Go to Menu [{datetime.now()}] \n')
        main()


elevate()
main()
f.close()
