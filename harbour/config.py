ADS_CLASSIC_URL = 'http://{mirror}/email={email}&password={password}'
ADS_CLASSIC_LIBRARIES_URL = 'http://{mirror}/cookie={cookie}'
ADS_CLASSIC_MIRROR_LIST = ['adstrio.cfa.harvard.edu', 'adsnun.cfa.harvard.edu', 'adsate.cfa.harvard.edu',
                           'astrobib.u-strasbg.fr', 'ads.nao.ac.jp', 'ads.astro.puc.cl', 'esoads.eso.org',
                           'ukads.nottingham.ac.uk', 'ads.iucaa.ernet.in', 'ads.inasan.ru', 'ads.bao.ac.cn',
                           'ads.mao.kiev.ua', 'ads.ari.uni-heidelberg.de', 'ads.arsip.lipi.go.id', 'ads.on.br',
                           'saaoads.chpc.ac.za', 'adsabs.harvard.edu']
SQLALCHEMY_BINDS = {'harbour': ''}

HARBOUR_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

