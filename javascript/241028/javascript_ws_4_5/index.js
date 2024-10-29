const countATag = document.querySelector('.countA')
const countBTag = document.querySelector('.countB')

const AImgTag = document.querySelector('#player1-img')
const BImgTag = document.querySelector('#player2-img')

const sectionTag = document.querySelector('.button-box')
const scissorsBtn = document.querySelector('#scissors-button')
const rockBtn = document.querySelector('#rock-button')
const paperBtn = document.querySelector('#paper-button')



function playGame(player1, player2) {
  if (player1 === '가위') {
    if (player2 === '바위') {
      countBTag.textContent += 1
      return 2;
    } else if (player2 === '보') {
      countATag.textContent += 1
      return 1;
    }
  } else if (player1 === '바위') {
    if (player2 === '가위') {
      countATag.textContent += 1
      return 1;
    } else if (player2 === '보') {
      countBTag.textContent += 1
      return 2;
    }
  } else if (player1 === '보') {
    if (player2 === '바위') {
      countATag.textContent += 1
      return 1;
    } else if (player2 === '가위') {
      countBTag.textContent += 1
      return 2;
    }
  }
  return 0;
}

const buttonClickHandler = (choice) => {
  document.querySelectorAll('section > button').forEach(button => button.disabled = true);

  const selectionImg = ["./img/scissors.png", "./img/rock.png", "./img/paper.png"]
  const selection = ['가위', '바위', '보'];

  let player2Index = 0
  let computerChoice = null
  const player2ImgChange = () => {
    player2Index = Math.floor(Math.random() * 3);
    BImgTag.setAttribute('src', selectionImg[player2Index])
    computerChoice = selection[player2Index];
  }

  const changeImg100 = setInterval(player2ImgChange, 100);

  setTimeout(() => {
    clearInterval(changeImg100)
    BImgTag.setAttribute('src', selectionImg[player2Index])

    const result = playGame(choice, computerChoice);
    if (result === 1) {
      alert("Player1 승리!");
    } else if (result === 2) {
      alert("Player2 승리!");
    } else {
      alert("무승부입니다!");
    }

    document.querySelectorAll('section > button').forEach(button => button.disabled = false)
  }, 3000)
}

scissorsBtn.addEventListener('click', () => buttonClickHandler('가위'))
rockBtn.addEventListener('click', () => buttonClickHandler('가위'))
paperBtn.addEventListener('click', () => buttonClickHandler('가위'))