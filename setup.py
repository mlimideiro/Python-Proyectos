import distutils.core 
import setup
import py2exe

setup(name="Calculo Variaciones",
 version="1.0",
 description="Calcula variacion entre temperaturas de CABA",
 author="Pía Tamporenea y Marcelo Limideirio",
 author_email="mlimideiro@gmail.com",
 url="none",
 license="none",
 scripts=["1.py"],
 console=["1.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
 )