import "../styles/StrategyCard.css";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";

interface StrategyCardProps {

    title: string;

    strategy: any;

}

function StrategyCard({

    title,

    strategy

}: StrategyCardProps) {

    if (!strategy) {

        return null;

    }

    const formatKey = (

        key: string

    ) => {

        return key

            .replace(/_/g, " ")

            .replace(/\b\w/g, c => c.toUpperCase());

    };

    return (

        <div className="strategy-card">

            <div className="strategy-header">

                <h2>

                    {title}

                </h2>

            </div>

            <div className="strategy-body">

                {

                    Object.entries(strategy).map(

                        ([key, value]) => (

                            <div

                                className="strategy-section"

                                key={key}

                            >

                                <h3>

                                    {formatKey(key)}

                                </h3>

                                <div className="strategy-content">

                                    {

                                        typeof value === "string"

                                        ?

                                        <ReactMarkdown
                                            remarkPlugins={[remarkGfm]}
                                            rehypePlugins={[rehypeHighlight]}
                                        >

                                            {String(value)}

                                        </ReactMarkdown>

                                        :

                                        <pre>

                                            {JSON.stringify(

                                                value,

                                                null,

                                                2

                                            )}

                                        </pre>

                                    }

                                </div>

                            </div>

                        )

                    )

                }

            </div>

        </div>

    );

}

export default StrategyCard;