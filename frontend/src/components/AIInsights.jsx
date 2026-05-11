function AIInsights({ failure }) {

    if (!failure) {

        return null;
    }

    return (

        <div className="
            bg-gray-800
            p-6
            rounded-2xl
            shadow-lg
            mt-8
        ">

            <h2 className="
                text-2xl
                font-bold
                mb-6
                text-white
            ">

                AI Debugging Insights

            </h2>

            <div className="space-y-6">

                <div>

                    <h3 className="
                        text-lg
                        font-semibold
                        text-blue-400
                    ">

                        Similar Failures

                    </h3>

                    <ul className="
                        list-disc
                        ml-6
                        mt-2
                        text-gray-300
                    ">

                        {failure.similar_errors?.map(
                            (error, index) => (

                                <li key={index}>
                                    {error}
                                </li>
                            )
                        )}

                    </ul>

                </div>

                <div>

                    <h3 className="
                        text-lg
                        font-semibold
                        text-green-400
                    ">

                        AI Recommendation

                    </h3>

                    <p className="
                        mt-2
                        text-gray-300
                        leading-7
                    ">

                        {
                            failure.contextual_ai_recommendation
                        }

                    </p>

                </div>

            </div>

        </div>
    );
}

export default AIInsights;