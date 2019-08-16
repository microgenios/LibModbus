from distutils.core import setup
setup(
  name = 'LibModbus',       
  packages = ['LibModbus'],   
  version = '0.1',      
  license='MIT',       
  description = 'LibModbus do Conversor Modbus para MQTT M1',   
  author = 'Fernando Simplicio',                  
  author_email = 'fernando@microgenios.com.br',     
  url = 'https://github.com/microgenios/LibModbus',  
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['Modbus', 'Microgenios', 'Conversor M1'],  
  install_requires=[           
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.7',
  ],
)