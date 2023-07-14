import Head from 'next/head'
import { useEffect } from 'react'
import Layout from "../components/Layout";
import Nav from "../components/Nav";
import { Space_Grotesk } from 'next/font/google'
import GitHubIcon from '../public/github.svg'
import LinkedInIcon from '../public/linkedin.svg'
import EmailIcon from '../public/email.svg'

const spaceGrotesk = Space_Grotesk({ subsets: ['latin'] })

export default function Home() {
  useEffect(() => {
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.add('dark')
    }
  }, [])

  return (
    <>
      <Layout>
        <Nav />
        <main className="h-[calc(100%_-_216px)] flex flex-col justify-center flex-1">
          <h1 className={`font-bold text-3xl text-indigo-600 dark:text-indigo-400 ${spaceGrotesk.className}`}>
            Hi!
          </h1>
          <h2 className={`font-bold text-3xl mb-5 {spaceGrotesk.className}`}>
            Welcome To My Website.
          </h2>
          <p className="mb-5">
            I'm Belit, Just developing stuff.
            I like cats 😺, and more cats 😸
          </p>
          <ul className="flex">
            <li className="block w-9 h-9 flex justify-center items-center mr-3 bg-indigo-100 dark:bg-indigo-400 rounded hover:bg-blue-600 dark:hover:bg-blue-600 transition-all hover:text-slate-100 dark:text-white">
              <a className="w-full h-full flex items-center justify-center" href="https://www.linkedin.com/in/belit-k" target="_blank" rel="noreferrer"><LinkedInIcon /></a>
            </li>
            <li className="block w-9 h-9 flex justify-center items-center mr-3 bg-indigo-100 dark:bg-indigo-400 rounded hover:bg-slate-700 dark:hover:bg-slate-700 transition-all hover:text-slate-100 dark:text-white">
              <a className="w-full h-full flex items-center justify-center" href="https://github.com/BelitK" target="_blank" rel="noreferrer"><GitHubIcon /></a>
            </li>
            <li className="block h-9 flex justify-center items-center mr-3 bg-indigo-100 dark:bg-indigo-400 rounded hover:bg-red-400 dark:hover:bg-red-400 transition-all hover:text-slate-100 dark:text-white">
              <a className="w-full h-full flex items-center justify-center px-4" href="mailto:belitberdelk@gmail.com"><EmailIcon className="transition-all" /> belitberdelk@gmail.com</a>


            </li></ul><ul className="flex pt-6 pl-4">
            <li><div className="pr-4"><img href="https://www.youracclaim.com/badges/bbe95a27-287b-401f-a145-e74458dda89b/public_url" src="https://images.credly.com/size/140x140/images/efbdc0d6-b46e-4e3c-8cf8-2314d8a5b971/GCC_badge_python_1000x1000.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.youracclaim.com/badges/32c76830-02e2-4de0-be9a-6d9576fd30a9/public_url" src="https://images.credly.com/size/140x140/images/ae2f5bae-b110-4ea1-8e26-77cf5f76c81e/GCC_badge_IT_Support_1000x1000.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.youracclaim.com/badges/0eb80a7d-aaa5-40d1-b46d-1fc8f6eb8e2d/public_url" src="https://images.credly.com/size/140x140/images/a8e890b4-d484-4e04-b521-fba516a8c3cd/coursera-specialization-badge.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.youracclaim.com/badges/94a0f774-310a-4909-bd8f-282f5cc0c6a0/public_url" src="https://images.credly.com/size/140x140/images/c2cc3091-c033-40c0-9cfc-2d5d78a3fa30/Applied_AI_with_Deep_Learning.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.credly.com/badges/2d9ddb4f-bd92-441e-88f4-7492a9649eba/public_url" src="https://images.credly.com/size/140x140/images/007afae6-2754-4a7c-9c44-e95c64c93656/IBM_Watson_IoT-_Advanced_Machine_Learning_and_Signal_Processing.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.youracclaim.com/badges/b27fbbe0-8829-4a67-808a-b7ca6edc4f9c/public_url" src="https://images.credly.com/size/140x140/images/d3d687ea-c3a8-43c8-96bb-704658c71a4a/Fundamentals_of_Scalable_Data_Science.png"></img></div></li>
            </ul><ul className="flex pt-6 pl-2">
            <li><div className="pr-4"><img href="https://www.credly.com/badges/5614d34f-be57-489b-9230-593375a0f55f/public_url" src="https://images.credly.com/size/140x140/images/fce226c2-0f13-4e17-b60c-24fa6ffd88cb/Intro2IoT.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.credly.com/badges/2892de3e-69ce-4817-b733-ccb57f0f6ef3/public_url" src="https://images.credly.com/size/140x140/images/af8c6b4e-fc31-47c4-8dcb-eb7a2065dc5b/I2CS__1_.png"></img></div></li>
            <li><div className="pr-4"><img href="https://www.credly.com/badges/aeec7df3-71ad-4b58-bc38-3fe2bd5c5627/public_url" src="https://images.credly.com/size/140x140/images/054913b2-e271-49a2-a1a4-9bf1c1f9a404/CyberEssentials.png"></img></div></li>
          </ul>
        </main>
      </Layout>
    </>
  )
}
