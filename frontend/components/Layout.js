import Head from "next/head";
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })


export default function Layout({ children }) {
  return (
    <>
      <Head>
        <title>Belit K.</title>
        <meta name="description" content="Belit Berdel Kış" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={`bg-slate-50 dark:bg-slate-800 min-h-screen text-gray-700 dark:text-gray-100 px-5 ${inter.className}`}>
        <div className="min-h-screen max-w-4xl mx-auto flex flex-col">{children}</div>
      </div>
    </>
  )
}
