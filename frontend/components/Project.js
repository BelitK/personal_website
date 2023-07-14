const Project = (props) => {
  const { name, desc, url } = props

  return (
    <article className="flex flex-col justify-between w-64 h-64 bg-indigo-50 m-3 border-2 border-indigo-200 border-dashed rounded-md box-border">
      <div>
        <h2 className="text-xl font-bold m-3">{name}</h2>
        <p className="m-3">{desc}</p>
      </div>
      <a className="bg-indigo-500 hover:bg-indigo-600 text-slate-50 p-3 block m-3 flex items-center rounded" href={url}>
        Project link
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5 ml-2">
          <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
        </svg>
      </a>
    </article>
  )
}

export default Project
