import { Support as SupportIcon } from '@repalis/orbit/icons'
import { schemas } from '@repalis/client'
import { useSidebar } from '@repalis/ui/components/atoms/Sidebar'
import { twMerge } from 'tailwind-merge'

import { FeedbackModal } from './FeedbackModal'
import { useSupportModal } from './useSupportModal'

export const SupportButton = ({
  organization,
}: {
  organization: schemas['Organization']
}) => {
  const { state } = useSidebar()
  const isCollapsed = state === 'collapsed'
  const { isShown, open, hide } = useSupportModal()

  return (
    <>
      <button
        type="button"
        onClick={open}
        className={twMerge(
          'flex cursor-pointer flex-row items-center rounded-lg border border-transparent px-2 text-sm transition-colors dark:border-transparent',
          'dark:text-repalis-500 dark:hover:text-repalis-200 text-gray-500 hover:text-black',
        )}
      >
        <SupportIcon fontSize="inherit" />
        {!isCollapsed && <span className="ml-4 font-medium">Support</span>}
      </button>
      <FeedbackModal
        isShown={isShown}
        hide={hide}
        organization={organization}
      />
    </>
  )
}
