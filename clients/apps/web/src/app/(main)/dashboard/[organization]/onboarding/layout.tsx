export default async function Layout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="dark:bg-repalis-950 flex h-full flex-col">{children}</div>
  )
}
