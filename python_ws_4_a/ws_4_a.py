# 아래에 코드를 작성하시오.
from conf.settings import NAME, MAIN_URL
from utils import create_url

result = create_url.create_url(NAME, MAIN_URL)
print(result)