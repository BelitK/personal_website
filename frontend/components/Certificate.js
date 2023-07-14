const Certificate = (props) => {
  const { id, name, date, url } = props

  return (
    <a href={url} target="_blank" rel="noreferrer">
      <article className="flex flex-col justify-between min-h-20 bg-indigo-50 m-3 border-2 border-indigo-200 border-dashed rounded-md box-border hover:border-indigo-300 hover:bg-indigo-100">
        <div>
          <h2 className="text-xl font-bold m-3 dark:text-slate-600"><span className="text-slate-400 mr-1">#{id}</span> {name}</h2>
          <p className="mx-3 mb-3 text-slate-400">{date} <b>·</b> <a href={url}>Link to Certificate</a></p>
        </div>
      </article>
    </a>
  )
}

export default Certificate
