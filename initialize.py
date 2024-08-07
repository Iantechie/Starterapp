import os
import shutil

class Initialize:
    help = 'Ininialize the app'

    bcolors = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKCYAN': '\033[96m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }
    
    def create_dir(self, dir_name):
        try:
            os.makedirs(dir_name)
            print("Created [{dir_name}] directory, proceding...".format(dir_name=dir_name))
        except OSError as err:
            print(f"{self.bcolors['FAIL']}Directory error: {err}{self.bcolors['ENDC']}".format(err=err))

    def copy_file(self, src_file, dest_file):
        try:
            if os.path.exists(dest_file) is True:
                print(f"{self.bcolors['WARNING']}File: [{dest_file}] already exists, proceding...{self.bcolors['ENDC']}".format(dest_file=dest_file))
            elif os.path.exists(src_file) is False:
                print(f"{self.bcolors['FAIL']}Error: file{self.bcolors['ENDC']} {self.bcolors['WARNING']}[{src_file}]{self.bcolors['ENDC']} {self.bcolors['FAIL']}does not exist.{self.bcolors['ENDC']}")
            else:
                shutil.copy(src_file, dest_file)
                print("Copied [{src_file}] file to [{dist_file}]".format(src_file=src_file, dist_file=dest_file))
        except shutil.SameFileError:
            print(f"{self.bcolors['FAIL']}Source and destination files cannot be same{self.bcolors['ENDC']}")
        except PermissionError as perm_err:
            print(f"{self.bcolors['FAIL']}Permission error: {self.bcolors['ENDC']}", perm_err)
        except:
            print(f"{self.bcolors['FAIL']}Error occurred while copying file.{self.bcolors['ENDC']}")

    def create_file(self, file_name):
        try:
            if os.path.exists(file_name) is False:
                open(file_name, 'a').close()  
                print("Created [{file_name}] file, proceding...".format(file_name=file_name))
            else:
                print(f"{self.bcolors['WARNING']}File: [{file_name}] already exists, proceding...{self.bcolors['ENDC']}".format(file_name=file_name))

        except IOError as err:
            print("File error: {err} ".format(err=err))

if __name__ == ('__main__'):

    ROOT_DIR = os.path.join(os.path.dirname(os.getcwd()), 'web_app')
    SETTINGS_DIR = os.path.join(os.path.dirname(os.getcwd()), 'web_app', 'web-app')
    SSO_DIR = os.path.join(os.path.dirname(os.getcwd()), 'web_app', 'sso')

    logs_dir = os.path.join(ROOT_DIR, 'logs/')
    sso_log_file = os.path.join(ROOT_DIR, 'logs/', 'sso.log')
    app_log_file = os.path.join(ROOT_DIR, 'logs/', 'app.log')

    src_local_settings = os.path.join(SETTINGS_DIR, 'local_settings.default')
    src_sso_setting_file = os.path.join(SETTINGS_DIR, 'settings_sso.default')
    dest_local_settings_file = os.path.join(SETTINGS_DIR, 'local_settings.py')
    dest_sso_setting_file = os.path.join(SETTINGS_DIR, 'settings_sso.py')

    src_saml_uri = os.path.join(SSO_DIR, 'attribute-maps', 'saml_uri.default')
    dest_saml_uri = os.path.join(SSO_DIR, 'attribute-maps', 'saml_uri.py')
    src_remote_meta = os.path.join(SSO_DIR, 'remote_metadata.xml.default')
    dest_remote_meta = os.path.join(SSO_DIR, 'remote_metadata.xml')


    initialize = Initialize()

    initialize.create_dir(logs_dir)
    initialize.create_file(sso_log_file)
    initialize.create_file(app_log_file)
    initialize.copy_file(src_local_settings, dest_local_settings_file)
    initialize.copy_file(src_sso_setting_file, dest_sso_setting_file)
    initialize.copy_file(src_saml_uri, dest_saml_uri)
    initialize.copy_file(src_remote_meta, dest_remote_meta)
        