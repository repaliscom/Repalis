import { Container, Preview } from 'react-email'
import RepalisHeader from '../RepalisHeader'
import WrapperBase from '../WrapperBase'

interface WrapperRepalisProps {
  children: React.ReactNode
  preview?: string
}

const WrapperRepalis = ({ children, preview }: WrapperRepalisProps) => {
  return (
    <WrapperBase>
      {preview ? <Preview>{preview}</Preview> : null}
      <Container className="px-[12px] pt-[20px] pb-[10px]">
        <RepalisHeader />
      </Container>
      <Container className="px-[20px] pt-[10px] pb-[20px]">
        {children}
      </Container>
    </WrapperBase>
  )
}

export default WrapperRepalis
