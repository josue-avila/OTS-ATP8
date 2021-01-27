import sys
sys.path.append('.')

from backend.models.base_model import BaseModel
from backend.models.marketplace import Marketplace

name = 'Marketplace teste'
description = 'Descrição teste'

marketplace = Marketplace(name, description)


def test_compare_column_model():
    assert marketplace.name == name
    assert marketplace.description == description


def test_compare_type_column_model():
    assert type(marketplace.name) == str
    assert type(marketplace.description) == str


def test_compare_isinstance():
    assert isinstance(marketplace, BaseModel)
    assert isinstance(marketplace, Marketplace)


def test_has_attribute():
    assert hasattr(marketplace, 'name')
    assert hasattr(marketplace, 'description')

def test_validate_name():
    try:
        Marketplace(None, 'testolist.com')
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_description():
    try:
        Marketplace('Test', """ Sou poeta e grande leitor de poesia, gosto, também, de ler crítica sobre isso, 
        mas tenho percebido, já há algum tempo, que alguns críticos estão confundindo gosto pessoal com qualidade 
        poética, o que denuncia que a poesia ainda vive em grupos de amigos que ficam se bolinando mutuamente e 
        pior ainda, na minha opinião, é que estão pregando a forma única, ou seja, querem que os poemas atuais 
        sejam cópias de uns poucos já conceituados.
        O linguista e professor Marcos Bagno, que é conhecido pelos seus livros que denunciam o preconceito 
        social por meio da linguagem, não faz ideia de que esse preconceito está agora na poesia. 
        Em algumas leituras percebo que aqueles que fazem poemas com uma linguagem mais simples e menos 
        apurada são tachados de negligentes em relação à arte poética, o que achariam, esses críticos, 
        dos poemas de Oswald de Andrade ou Mário Quintana se publicassem hoje?
        Muitos críticos pregam o hermetismo poético, poema bom é poema ininteligível para a maioria. 
        Eu não posso concordar, por minha militância na democratização da poesia. 
        Democratização não é a facilitação. Não. É o convite através de uma linguagem mais simples, 
        longe da simplória, àqueles que não têm o costume da leitura de poemas, ou usando um termo de 
        um amigo meu: Pregar aos não convertidos. O meu sonho é que a poesia ganhe as ruas, de modo 
        mais literal possível.
        Não faço apologia à poema de má qualidade, descuidada, mas prego a diversidade de linguagem, 
        já imaginaram as pessoas nos escritórios, nos salões de cabeleireiros, ou em qualquer outra 
        parte conversando sobre poesia em vez de conversar sobre a novela das oito? Sonho? Se depender 
        dos críticos sim, porque o preconceito social jamais permitirá que a poesia fosse algo popular 
        e não de uma elite. (Esta é uma cópia para teste)
        """)
    except Exception as e:
        assert isinstance(e, ValueError)
