import { onTestFinished } from 'vitest'

export const listenToParentMessages = () => {
  const messages: Record<string, unknown>[] = []
  const listener = (event: MessageEvent) => {
    messages.push(event.data)
  }
  window.addEventListener('message', listener)
  onTestFinished(() => window.removeEventListener('message', listener))
  return messages
}

export const getEmbedCloseButton = (): HTMLButtonElement => {
  const layout = document.getElementById('repalis-embed-layout')
  const content = document.getElementById('repalis-embed-content')
  const button = Array.from(layout?.querySelectorAll('button') ?? []).find(
    (candidate) => !content?.contains(candidate),
  )
  if (!button) {
    throw new Error('Embed close button not rendered')
  }
  return button
}
