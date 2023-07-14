import Layout from '../components/Layout'
import Nav from '../components/Nav'
import Certificate from '../components/Certificate'

const Certificates = ({ data }) => {
  return (
    <Layout>
      <Nav />
      <div className="">
        {data?.map(certificate => (
          <Certificate
            key={certificate.id}
            id={certificate.id}
            name={certificate.name}
            date={certificate.Date}
            url={certificate.Cred_URL}
          />
        ))}
      </div>
    </Layout>
  )
}

export async function getServerSideProps() {
  const res = await fetch(`http://api:1000/certs`)
  const data = await res.json()

  return { props: { data } }
}

export default Certificates
