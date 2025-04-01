
import { useState } from 'react'
import './App.css'

const inspirationCards = [
  {
    title: '听觉任务',
    description: '闭上眼，记录你身边3种不同的声音。',
    emotion: '静心 / 听觉',
  },
  {
    title: '图像任务',
    description: '拍一张“最不显眼的颜色”照片，为它写一个故事标题。',
    emotion: '好奇 / 视觉',
  },
  {
    title: '身体任务',
    description: '用身体摆出一个你今天的情绪姿势，自拍下来存档。',
    emotion: '表达 / 行动',
  },
  {
    title: '写作任务',
    description: '写下一句你今天想对世界说的话，不用解释。',
    emotion: '宣泄 / 内心',
  },
]

function App() {
  const [card, setCard] = useState(null)

  const drawCard = () => {
    const random = Math.floor(Math.random() * inspirationCards.length)
    setCard(inspirationCards[random])
  }

  return (
    <div className="App">
      <h1>🎴 抽一张今日的灵感卡片</h1>
      <button onClick={drawCard}>开始抽卡</button>
      {card && (
        <div className="card">
          <h2>{card.title}</h2>
          <p>{card.description}</p>
          <span>情绪关键词：{card.emotion}</span>
        </div>
      )}
    </div>
  )
}

export default App
