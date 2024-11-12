import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('counter', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
  ])

  const findBalance = (targetName) => {
    return computed(() => {
      return balances.value.find(balance => balance.name === targetName)
    })
  }

  const increaseBalance = (targetName) => {
    const target = balances.value.find(balance => balance.name === targetName)
    if (target) {
      target.balance += 1000
    }
  }

  return { balances, findBalance, increaseBalance }
})
