import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer
} from "recharts";

function AnalyticsCharts({ failures }) {

    const severityData = [

        {
            name: "HIGH",

            value: failures.filter(
                failure =>
                    failure.severity === "HIGH"
            ).length
        },

        {
            name: "MEDIUM",

            value: failures.filter(
                failure =>
                    failure.severity === "MEDIUM"
            ).length
        },

        {
            name: "LOW",

            value: failures.filter(
                failure =>
                    failure.severity === "LOW"
            ).length
        }
    ];

    const COLORS = [
        "#ef4444",
        "#facc15",
        "#22c55e"
    ];

    return (

        <div className="
            bg-gray-800
            rounded-2xl
            p-6
            shadow-lg
            mt-8
        ">

            <h2 className="
                text-2xl
                font-bold
                text-white
                mb-6
            ">

                Failure Severity Analytics

            </h2>

            <div
                style={{
                    width: "100%",
                    height: 350
                }}
            >

                <ResponsiveContainer>

                    <PieChart>

                        <Pie
                            data={severityData}

                            dataKey="value"

                            nameKey="name"

                            outerRadius={120}

                            label
                        >

                            {severityData.map(
                                (entry, index) => (

                                    <Cell
                                        key={index}

                                        fill={
                                            COLORS[index]
                                        }
                                    />
                                )
                            )}

                        </Pie>

                        <Tooltip />

                    </PieChart>

                </ResponsiveContainer>

            </div>

        </div>
    );
}

export default AnalyticsCharts;