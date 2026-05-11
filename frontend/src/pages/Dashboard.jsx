import { useEffect, useState } from "react";

import API from "../services/api";

import StatsCard from "../components/StatsCard";

import AIInsights from "../components/AIInsights";

import AnalyticsCharts from "../components/AnalyticsCharts";

function Dashboard() {

    const [failures, setFailures] = useState([]);

    const [selectedFailure, setSelectedFailure] =
        useState(null);

    useEffect(() => {

        fetchFailures();

    }, []);

    const fetchFailures = async () => {

        try {

            const response =
                await API.get("/failure-history");

            setFailures(response.data);

        } catch (error) {

            console.error(
                "Error fetching failures",
                error
            );
        }
    };

    const totalFailures = failures.length;

    const highSeverity = failures.filter(
        failure =>
            failure.severity === "HIGH"
    ).length;

    const authIssues = failures.filter(
        failure =>
            failure.category === "AUTH"
    ).length;

    return (

        <div className="
            min-h-screen
            bg-gray-900
            text-white
            p-8
        ">

            <h1 className="
                text-5xl
                font-bold
                mb-10
            ">

                IntelliDebug AI Dashboard

            </h1>

            <div className="
                grid
                grid-cols-1
                md:grid-cols-3
                gap-6
                mb-10
            ">

                <StatsCard
                    title="Total Failures"
                    value={totalFailures}
                />

                <StatsCard
                    title="High Severity"
                    value={highSeverity}
                />

                <StatsCard
                    title="Auth Issues"
                    value={authIssues}
                />

            </div>

            <div className="
                bg-gray-800
                rounded-2xl
                p-6
                shadow-lg
            ">

                <h2 className="
                    text-3xl
                    font-semibold
                    mb-6
                ">

                    Failure History

                </h2>

                <table className="w-full">

                    <thead>

                        <tr className="
                            text-left
                            border-b
                            border-gray-700
                        ">

                            <th className="p-3">
                                Error
                            </th>

                            <th className="p-3">
                                Category
                            </th>

                            <th className="p-3">
                                Severity
                            </th>

                            <th className="p-3">
                                Confidence
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {failures.map((failure) => (

                            <tr
                                key={failure.id}

                                onClick={() =>
                                    setSelectedFailure(
                                        failure
                                    )
                                }

                                className="
                                    border-b
                                    border-gray-700
                                    cursor-pointer
                                    hover:bg-gray-700
                                    transition
                                "
                            >

                                <td className="p-3">

                                    {
                                        failure.error_message
                                    }

                                </td>

                                <td className="p-3">

                                    {
                                        failure.category
                                    }

                                </td>

                                <td className="p-3">

                                    <span className={`
                                        px-3
                                        py-1
                                        rounded-full
                                        text-sm
                                        font-semibold

                                        ${
                                            failure.severity === "HIGH"

                                            ? "bg-red-500"

                                            : failure.severity === "MEDIUM"

                                            ? "bg-yellow-500"

                                            : "bg-green-500"
                                        }
                                    `}>

                                        {
                                            failure.severity
                                        }

                                    </span>

                                </td>

                                <td className="p-3">

                                    {
                                        failure.confidence_score
                                    }

                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

            <AIInsights
                failure={selectedFailure}
            />

            <AnalyticsCharts
                failures={failures}
            />

        </div>
    );
}

export default Dashboard;