/* 
  아래에 코드를 작성해주세요.
*/
const API_KEY = '733a96524110d95b6f4f481d0a55c774'
const searchBtn = document.querySelector('.search-box__button')

const fetchAlbums = function (page=1, limit=10) {
  // alert('확인!')
  const resultDivTag = document.querySelector('.search-result')
  resultDivTag.textContent = ''

  const keyword = document.querySelector('.search-box__input').value
  console.log(keyword)

  axios ({
    method: 'get',
    url: `http://ws.audioscrobbler.com/2.0/`,
    params: {
      method: 'album.search',
      format: 'json',
      album: keyword,
      api_key: API_KEY,
    }
  })
    .then((response) => {
      // console.log(response)
      const albums = response.data.results.albummatches.album
      console.log(albums)
      if (albums.length === 0) {
        alert('잠시 후 다시 시도해주세요.')
      } else {

        albums.forEach((album) => {
          const h2Tag = document.createElement('h2')
          h2Tag.textContent = album.artist

          const pTag = document.createElement('p')
          pTag.textContent = album.name

          const textResultDivTag = document.createElement('div')
          textResultDivTag.classList.add('search-result__text')
          textResultDivTag.appendChild(h2Tag)
          textResultDivTag.appendChild(pTag)

          const imgTag = document.createElement('img')

          imgTag.setAttribute('src', album.image[1]['#text'])

          const cardResultDivTag = document.createElement('div')
          cardResultDivTag.classList.add('search-result__card')
          cardResultDivTag.appendChild(imgTag)
          cardResultDivTag.appendChild(textResultDivTag)
          
          const aTag = document.createElement('a')
          aTag.setAttribute('href', album.url)
          aTag.style.textDecorationLine = 'none'
          aTag.style.color = 'black'

          aTag.appendChild(cardResultDivTag)

          resultDivTag.appendChild(aTag)
        })
      }
    })
    .catch((error) => {
      console.log(error)
    })
}

searchBtn.addEventListener('click', fetchAlbums)