import Link from "next/link";
import { Space_Grotesk } from 'next/font/google'

const spaceGrotesk = Space_Grotesk({ subsets: ['latin'] })

export default function Nav() {
  const changeTheme = () => {
    const theme = localStorage.getItem('theme')
    if (theme === 'dark') {
      localStorage.setItem('theme', 'light')
      document.documentElement.classList.remove('dark')
    } else {
      localStorage.setItem('theme', 'dark')
      document.documentElement.classList.add('dark')
    }
  }

  return (
    <nav>
      <ul className="flex flex-col text-xl py-10 sm:flex-row">
        <li className="font-medium text-gray-500 dark:text-indigo-400 mr-6">Belit Berdel Kış</li>
        <li className={`font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-all mr-6 ${spaceGrotesk.className}`}><Link href="/">Home</Link></li>
        <li className={`font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-all mr-6 ${spaceGrotesk.className}`}><Link href="/projects">Projects</Link></li>
        <li className={`font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-all mr-6 ${spaceGrotesk.className}`}><Link href="/certificates">Certificates</Link></li>
        <li className={`font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-all ${spaceGrotesk.className}`}><button onClick={changeTheme}>DarkMode</button></li>
      </ul>
    </nav>
  )
}
