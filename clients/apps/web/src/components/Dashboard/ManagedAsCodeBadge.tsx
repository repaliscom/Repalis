import { LockOutlined } from '@repalis/orbit/icons'
import { Pill } from '@repalis/orbit'

export const ManagedAsCodeBadge = () => (
  <Pill color="gray">
    <LockOutlined fontSize="inherit" />
    <span>Managed in code</span>
  </Pill>
)
