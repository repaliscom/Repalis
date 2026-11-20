import { afterEach, beforeAll, describe, expect, it, vi } from 'vitest'
import { RepalisEmbedPaymentMethod } from './payment-method'

const ALLOWED_ORIGIN = 'http://127.0.0.1:3000'
const CUSTOMER_SESSION_TOKEN = 'polar_cst_test_token'

beforeAll(() => {
  // @ts-expect-error - Global defined at build time by tsdown
  globalThis.__REPALIS_CHECKOUT_EMBED_SCRIPT_ALLOWED_ORIGINS__ = ALLOWED_ORIGIN
})

const cleanupDom = () => {
  document.querySelectorAll('iframe').forEach((el) => el.remove())
  document.querySelectorAll('style').forEach((el) => el.remove())
  document.querySelectorAll('div').forEach((el) => el.remove())
  document.body.classList.remove('repalis-no-scroll')
}

const dispatchLoaded = () => {
  window.dispatchEvent(
    new MessageEvent('message', {
      origin: ALLOWED_ORIGIN,
      data: { type: 'REPALIS_PAYMENT_METHOD', event: 'loaded' },
    }),
  )
}

describe('RepalisEmbedPaymentMethod', () => {
  describe('postMessage', () => {
    it('posts a message to the parent window with the correct type', () => {
      const postMessageSpy = vi.spyOn(window.parent, 'postMessage')

      RepalisEmbedPaymentMethod.postMessage({ event: 'loaded' }, ALLOWED_ORIGIN)

      expect(postMessageSpy).toHaveBeenCalledWith(
        { event: 'loaded', type: 'REPALIS_PAYMENT_METHOD' },
        ALLOWED_ORIGIN,
      )

      postMessageSpy.mockRestore()
    })

    it('includes event data for success messages', () => {
      const postMessageSpy = vi.spyOn(window.parent, 'postMessage')

      RepalisEmbedPaymentMethod.postMessage(
        { event: 'success', paymentMethodId: 'pm_123' },
        ALLOWED_ORIGIN,
      )

      expect(postMessageSpy).toHaveBeenCalledWith(
        {
          event: 'success',
          paymentMethodId: 'pm_123',
          type: 'REPALIS_PAYMENT_METHOD',
        },
        ALLOWED_ORIGIN,
      )

      postMessageSpy.mockRestore()
    })
  })

  describe('create', () => {
    afterEach(cleanupDom)

    it('creates an iframe with the correct src and modal mode', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')
      expect(iframe).not.toBeNull()

      const src = new URL(iframe!.src)
      expect(src.pathname).toBe('/embed/payment-method')
      expect(src.origin).toBe(ALLOWED_ORIGIN)
      expect(src.searchParams.get('session_token')).toBe(CUSTOMER_SESSION_TOKEN)
      expect(src.searchParams.get('embed')).toBe('true')
      expect(src.searchParams.get('embed_origin')).toBe(window.location.origin)
      expect(src.searchParams.get('mode')).toBe('modal')
      expect(iframe!.style.colorScheme).toBe('light')

      embed.close()
    })

    it('sets theme query parameter when provided', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
        theme: 'dark',
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')
      const src = new URL(iframe!.src)
      expect(src.searchParams.get('theme')).toBe('dark')
      expect(iframe!.style.colorScheme).toBe('dark')

      embed.close()
    })

    it('sets set_default=false when setAsDefault is explicitly false', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
        setAsDefault: false,
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')!
      expect(new URL(iframe.src).searchParams.get('set_default')).toBe('false')

      embed.close()
    })

    it('omits set_default URL param by default', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')!
      expect(new URL(iframe.src).searchParams.get('set_default')).toBeNull()

      embed.close()
    })

    it('forwards a member token verbatim — no client-side type sniffing', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: 'polar_mst_test_member',
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')!
      const src = new URL(iframe.src)
      expect(src.searchParams.get('session_token')).toBe(
        'polar_mst_test_member',
      )

      embed.close()
    })

    it('adds repalis-no-scroll class to body', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      expect(document.body.classList.contains('repalis-no-scroll')).toBe(true)

      dispatchLoaded()
      const embed = await promise
      embed.close()
    })

    it('opts the overlay out of Lenis smooth scrolling', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      expect(
        document.querySelector('iframe')!.getAttribute('data-lenis-prevent'),
      ).toBe('')

      dispatchLoaded()
      const embed = await promise
      embed.close()
    })

    it('calls onLoaded callback when the embed loads', async () => {
      const onLoaded = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
        onLoaded,
      })

      dispatchLoaded()
      const embed = await promise

      expect(onLoaded).toHaveBeenCalledTimes(1)
      embed.close()
    })
  })

  describe('close', () => {
    afterEach(cleanupDom)

    it('removes the iframe from the DOM', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      expect(document.querySelector('iframe')).not.toBeNull()
      embed.close()
      expect(document.querySelector('iframe')).toBeNull()
    })

    it('removes repalis-no-scroll class from body', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.close()

      expect(document.body.classList.contains('repalis-no-scroll')).toBe(false)
    })
  })

  describe('event handling', () => {
    afterEach(cleanupDom)

    it('dispatches close event and removes iframe', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'close' },
        }),
      )

      expect(document.querySelector('iframe')).toBeNull()
      embed.close()
    })

    it('prevents close after confirmed event', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'confirmed' },
        }),
      )
      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'close' },
        }),
      )

      expect(document.querySelector('iframe')).not.toBeNull()
      embed.close()
    })

    it('auto-closes the modal on success', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'confirmed' },
        }),
      )
      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: {
            type: 'REPALIS_PAYMENT_METHOD',
            event: 'success',
            paymentMethodId: 'pm_123',
          },
        }),
      )

      expect(document.querySelector('iframe')).toBeNull()
      embed.close()
    })

    it('skips the default auto-close when success listener calls preventDefault', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('success', (event) => event.preventDefault())

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: {
            type: 'REPALIS_PAYMENT_METHOD',
            event: 'success',
            paymentMethodId: 'pm_123',
          },
        }),
      )

      expect(document.querySelector('iframe')).not.toBeNull()
      embed.close()
    })

    it('forwards success event detail to listeners', async () => {
      const successListener = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('success', successListener)

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: {
            type: 'REPALIS_PAYMENT_METHOD',
            event: 'success',
            paymentMethodId: 'pm_abc',
          },
        }),
      )

      expect(successListener).toHaveBeenCalledTimes(1)
      const event = successListener.mock.calls[0][0] as CustomEvent
      expect(event.detail.paymentMethodId).toBe('pm_abc')

      embed.close()
    })

    it('forwards error event detail to listeners', async () => {
      const errorListener = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('error', errorListener)

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: {
            type: 'REPALIS_PAYMENT_METHOD',
            event: 'error',
            code: 'unauthorized',
          },
        }),
      )

      expect(errorListener).toHaveBeenCalledTimes(1)
      expect((errorListener.mock.calls[0][0] as CustomEvent).detail.code).toBe(
        'unauthorized',
      )

      embed.close()
    })

    it('silently drops resize messages in modal mode', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise

      const iframe = document.querySelector('iframe')!
      const heightBefore = iframe.style.height

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: {
            type: 'REPALIS_PAYMENT_METHOD',
            event: 'resize',
            height: 480,
          },
        }),
      )

      expect(iframe.style.height).toBe(heightBefore)
      embed.close()
    })

    it('ignores messages from disallowed origins', async () => {
      const closeListener = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('close', closeListener)

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: 'https://evil.com',
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'close' },
        }),
      )

      expect(closeListener).not.toHaveBeenCalled()
      expect(document.querySelector('iframe')).not.toBeNull()

      embed.close()
    })

    it('ignores messages with the wrong type', async () => {
      const closeListener = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('close', closeListener)

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_CHECKOUT', event: 'close' },
        }),
      )

      expect(closeListener).not.toHaveBeenCalled()
      embed.close()
    })

    it('skips the default close action when preventDefault is called', async () => {
      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('close', (event) => event.preventDefault())

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'close' },
        }),
      )

      expect(document.querySelector('iframe')).not.toBeNull()
      embed.close()
    })
  })

  describe('addEventListener / removeEventListener', () => {
    afterEach(cleanupDom)

    it('removes event listeners', async () => {
      const listener = vi.fn()

      const promise = RepalisEmbedPaymentMethod.create({
        sessionToken: CUSTOMER_SESSION_TOKEN,
      })

      dispatchLoaded()
      const embed = await promise
      embed.addEventListener('confirmed', listener)
      embed.removeEventListener('confirmed', listener)

      window.dispatchEvent(
        new MessageEvent('message', {
          origin: ALLOWED_ORIGIN,
          data: { type: 'REPALIS_PAYMENT_METHOD', event: 'confirmed' },
        }),
      )

      expect(listener).not.toHaveBeenCalled()
      embed.close()
    })
  })

  describe('init', () => {
    afterEach(() => {
      document
        .querySelectorAll('[data-repalis-payment-method]')
        .forEach((el) => el.remove())
      cleanupDom()
    })

    it('attaches click handlers that open the embed with the token', () => {
      const button = document.createElement('button')
      button.setAttribute('data-repalis-payment-method', CUSTOMER_SESSION_TOKEN)
      document.body.appendChild(button)

      RepalisEmbedPaymentMethod.init()

      button.click()

      const iframe = document.querySelector('iframe')
      expect(iframe).not.toBeNull()
      const src = new URL(iframe!.src)
      expect(src.searchParams.get('session_token')).toBe(CUSTOMER_SESSION_TOKEN)
    })

    it('reads theme from data-repalis-payment-method-theme', () => {
      const button = document.createElement('button')
      button.setAttribute('data-repalis-payment-method', CUSTOMER_SESSION_TOKEN)
      button.setAttribute('data-repalis-payment-method-theme', 'dark')
      document.body.appendChild(button)

      RepalisEmbedPaymentMethod.init()
      button.click()

      const iframe = document.querySelector('iframe')
      const src = new URL(iframe!.src)
      expect(src.searchParams.get('theme')).toBe('dark')
    })

    it('does nothing when the data attribute is empty', () => {
      const button = document.createElement('button')
      button.setAttribute('data-repalis-payment-method', '')
      document.body.appendChild(button)

      RepalisEmbedPaymentMethod.init()
      button.click()

      expect(document.querySelector('iframe')).toBeNull()
    })
  })

  describe('window.Polar', () => {
    it('exposes EmbedPaymentMethod on window.Polar', () => {
      expect(window.Polar).toBeDefined()
      expect(window.Polar.EmbedPaymentMethod).toBe(RepalisEmbedPaymentMethod)
    })
  })
})
