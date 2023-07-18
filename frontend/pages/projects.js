import Layout from '../components/Layout'
import Nav from '../components/Nav'
import Project from '../components/Project'

const Projects = () => {
  return (
    <>
      <Layout>
        <Nav />
        <main className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 max-w-max mx-auto dark:text-slate-600">
          <Project name="Vision Api" desc="Api implementation for vision ml" url="https://github.com/BelitK/VisionApi" />
          <Project name="E-Commerce Volume Comparison" desc="A comparison between turkish and american e-commerce market volumes" url="https://github.com/BelitK/E-CommerceVolume" />
          <Project name="BlockchainExample" desc="Blockchain example project" url="https://github.com/BelitK/blockchainexample" />
          <Project name="Fire Detection Project" desc="Fire detection using Yolov3, live project can be found at api.belitk.com" url="https://github.com/BelitK/MLcourse" />
          <Project name="Personel Website" desc="Personel Website" url="https://github.com/BelitK/personel_website" />
        </main>
      </Layout>
    </>
  )
}

export default Projects
