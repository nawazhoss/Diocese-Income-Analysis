import React, { useState, useMemo } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, ScatterChart, Scatter, Legend, TreemapChart, Treemap } from 'recharts';

const DioceseDashboard = () => {
  const [selectedView, setSelectedView] = useState('ranking');
  
  // Raw data from the CSV
  const rawData = [
    { diocese: "Bath & Wells", totalGiving: 13671, taxRecovered: 2615, legacies: 2365, grants: 2868, fundraising: 1476, trading: 1126, investment: 1098, statutoryFees: 2875, other: 2311, totalIncome: 30405 },
    { diocese: "Birmingham", totalGiving: 8566, taxRecovered: 1593, legacies: 850, grants: 2263, fundraising: 534, trading: 1346, investment: 555, statutoryFees: 2803, other: 2458, totalIncome: 20968 },
    { diocese: "Blackburn", totalGiving: 10403, taxRecovered: 1938, legacies: 1327, grants: 2343, fundraising: 1205, trading: 946, investment: 1064, statutoryFees: 1818, other: 1524, totalIncome: 22567 },
    { diocese: "Bristol", totalGiving: 9742, taxRecovered: 1759, legacies: 736, grants: 2173, fundraising: 694, trading: 1084, investment: 425, statutoryFees: 2998, other: 1132, totalIncome: 20746 },
    { diocese: "Canterbury", totalGiving: 8429, taxRecovered: 1566, legacies: 1569, grants: 1223, fundraising: 1221, trading: 812, investment: 697, statutoryFees: 1414, other: 1014, totalIncome: 17945 },
    { diocese: "Carlisle", totalGiving: 5912, taxRecovered: 1100, legacies: 1090, grants: 1385, fundraising: 617, trading: 667, investment: 653, statutoryFees: 662, other: 619, totalIncome: 12707 },
    { diocese: "Chelmsford", totalGiving: 18328, taxRecovered: 3196, legacies: 3350, grants: 4442, fundraising: 2438, trading: 3097, investment: 1254, statutoryFees: 7092, other: 1811, totalIncome: 45008 },
    { diocese: "Chester", totalGiving: 15185, taxRecovered: 2999, legacies: 1905, grants: 1899, fundraising: 1196, trading: 1367, investment: 1512, statutoryFees: 3085, other: 2391, totalIncome: 31539 },
    { diocese: "Chichester", totalGiving: 21938, taxRecovered: 3759, legacies: 4171, grants: 3700, fundraising: 1896, trading: 2705, investment: 1200, statutoryFees: 4128, other: 2001, totalIncome: 45498 },
    { diocese: "Coventry", totalGiving: 7335, taxRecovered: 1433, legacies: 2102, grants: 2821, fundraising: 590, trading: 902, investment: 728, statutoryFees: 1967, other: 393, totalIncome: 18271 },
    { diocese: "Derby", totalGiving: 6608, taxRecovered: 1236, legacies: 853, grants: 984, fundraising: 818, trading: 747, investment: 847, statutoryFees: 1160, other: 842, totalIncome: 14094 },
    { diocese: "Durham", totalGiving: 5910, taxRecovered: 1160, legacies: 610, grants: 2596, fundraising: 701, trading: 514, investment: 727, statutoryFees: 1326, other: 489, totalIncome: 14032 },
    { diocese: "Ely", totalGiving: 10502, taxRecovered: 1842, legacies: 733, grants: 1928, fundraising: 902, trading: 1119, investment: 631, statutoryFees: 1989, other: 930, totalIncome: 20575 },
    { diocese: "Exeter", totalGiving: 12618, taxRecovered: 2239, legacies: 1884, grants: 3070, fundraising: 1528, trading: 1613, investment: 1206, statutoryFees: 1874, other: 1151, totalIncome: 27183 },
    { diocese: "Gloucester", totalGiving: 10346, taxRecovered: 1797, legacies: 1818, grants: 1499, fundraising: 882, trading: 926, investment: 928, statutoryFees: 941, other: 1314, totalIncome: 20451 },
    { diocese: "Guildford", totalGiving: 19892, taxRecovered: 3725, legacies: 1804, grants: 2172, fundraising: 976, trading: 2015, investment: 789, statutoryFees: 4782, other: 737, totalIncome: 36892 },
    { diocese: "Hereford", totalGiving: 4514, taxRecovered: 805, legacies: 413, grants: 1281, fundraising: 1037, trading: 556, investment: 696, statutoryFees: 340, other: 494, totalIncome: 10135 },
    { diocese: "Leicester", totalGiving: 6302, taxRecovered: 1236, legacies: 733, grants: 1299, fundraising: 908, trading: 753, investment: 543, statutoryFees: 1375, other: 876, totalIncome: 14025 },
    { diocese: "Lichfield", totalGiving: 12110, taxRecovered: 2111, legacies: 1719, grants: 2439, fundraising: 1672, trading: 1292, investment: 1903, statutoryFees: 2182, other: 716, totalIncome: 26143 },
    { diocese: "Lincoln", totalGiving: 6099, taxRecovered: 1096, legacies: 2490, grants: 2730, fundraising: 1472, trading: 1281, investment: 955, statutoryFees: 1325, other: 1511, totalIncome: 18958 },
    { diocese: "Liverpool", totalGiving: 8538, taxRecovered: 1470, legacies: 1716, grants: 2155, fundraising: 776, trading: 807, investment: 966, statutoryFees: 2807, other: 742, totalIncome: 19976 },
    { diocese: "London", totalGiving: 58232, taxRecovered: 8681, legacies: 5548, grants: 17141, fundraising: 4604, trading: 11666, investment: 991, statutoryFees: 27371, other: 5438, totalIncome: 139674 },
    { diocese: "Manchester", totalGiving: 9158, taxRecovered: 1750, legacies: 648, grants: 1964, fundraising: 1204, trading: 936, investment: 718, statutoryFees: 2378, other: 1022, totalIncome: 19780 },
    { diocese: "Newcastle", totalGiving: 5186, taxRecovered: 971, legacies: 683, grants: 1061, fundraising: 661, trading: 386, investment: 407, statutoryFees: 1002, other: 432, totalIncome: 10790 },
    { diocese: "Norwich", totalGiving: 9026, taxRecovered: 1651, legacies: 2299, grants: 2806, fundraising: 1546, trading: 727, investment: 1095, statutoryFees: 1380, other: 1141, totalIncome: 21671 },
    { diocese: "Oxford", totalGiving: 35659, taxRecovered: 6509, legacies: 4538, grants: 6702, fundraising: 2678, trading: 4219, investment: 2057, statutoryFees: 4677, other: 2055, totalIncome: 69094 },
    { diocese: "Peterborough", totalGiving: 8083, taxRecovered: 1530, legacies: 1247, grants: 1256, fundraising: 1314, trading: 1236, investment: 705, statutoryFees: 855, other: 765, totalIncome: 16991 },
    { diocese: "Portsmouth", totalGiving: 6078, taxRecovered: 1004, legacies: 751, grants: 1903, fundraising: 782, trading: 675, investment: 459, statutoryFees: 2334, other: 628, totalIncome: 14615 },
    { diocese: "Rochester", totalGiving: 14267, taxRecovered: 2622, legacies: 1477, grants: 1376, fundraising: 1267, trading: 2131, investment: 834, statutoryFees: 4138, other: 1322, totalIncome: 29433 },
    { diocese: "St.Albans", totalGiving: 16643, taxRecovered: 3322, legacies: 1408, grants: 3066, fundraising: 2272, trading: 2234, investment: 1146, statutoryFees: 3113, other: 1689, totalIncome: 34893 },
    { diocese: "St.Edmundsbury & Ipswich", totalGiving: 8097, taxRecovered: 1528, legacies: 1364, grants: 2179, fundraising: 1380, trading: 919, investment: 829, statutoryFees: 1292, other: 1183, totalIncome: 18772 },
    { diocese: "Salisbury", totalGiving: 14396, taxRecovered: 2492, legacies: 1884, grants: 3075, fundraising: 1987, trading: 1595, investment: 1211, statutoryFees: 1905, other: 1754, totalIncome: 30298 },
    { diocese: "Sheffield", totalGiving: 8710, taxRecovered: 1533, legacies: 323, grants: 1791, fundraising: 568, trading: 617, investment: 814, statutoryFees: 1602, other: 538, totalIncome: 16497 },
    { diocese: "Sodor and Man", totalGiving: 816, taxRecovered: 0, legacies: 84, grants: 59, fundraising: 228, trading: 162, investment: 56, statutoryFees: 95, other: 114, totalIncome: 1615 },
    { diocese: "Southwark", totalGiving: 27615, taxRecovered: 4931, legacies: 2680, grants: 4277, fundraising: 1458, trading: 5344, investment: 743, statutoryFees: 11050, other: 4417, totalIncome: 62516 },
    { diocese: "Southwell & Nottingham", totalGiving: 8531, taxRecovered: 1569, legacies: 459, grants: 2282, fundraising: 702, trading: 858, investment: 693, statutoryFees: 1845, other: 720, totalIncome: 17660 },
    { diocese: "Truro", totalGiving: 4212, taxRecovered: 802, legacies: 825, grants: 995, fundraising: 613, trading: 655, investment: 617, statutoryFees: 618, other: 557, totalIncome: 9894 },
    { diocese: "Winchester", totalGiving: 13776, taxRecovered: 2684, legacies: 1817, grants: 2075, fundraising: 1353, trading: 1292, investment: 801, statutoryFees: 3112, other: 1912, totalIncome: 28822 },
    { diocese: "Worcester", totalGiving: 6078, taxRecovered: 1058, legacies: 2195, grants: 3382, fundraising: 696, trading: 890, investment: 790, statutoryFees: 990, other: 708, totalIncome: 16788 },
    { diocese: "York", totalGiving: 11146, taxRecovered: 1993, legacies: 2524, grants: 3120, fundraising: 1585, trading: 1208, investment: 1214, statutoryFees: 1751, other: 1149, totalIncome: 25690 },
    { diocese: "Leeds", totalGiving: 17329, taxRecovered: 3161, legacies: 2243, grants: 3568, fundraising: 2153, trading: 1634, investment: 1468, statutoryFees: 4187, other: 1835, totalIncome: 37578 }
  ];

  // Process data for different visualizations
  const sortedData = useMemo(() => {
    return [...rawData].sort((a, b) => b.totalIncome - a.totalIncome);
  }, []);

  const top10Data = useMemo(() => {
    return sortedData.slice(0, 10);
  }, [sortedData]);

  const incomeSourceData = useMemo(() => {
    const totalsBySource = rawData.reduce((acc, diocese) => {
      acc.totalGiving += diocese.totalGiving;
      acc.taxRecovered += diocese.taxRecovered;
      acc.legacies += diocese.legacies;
      acc.grants += diocese.grants;
      acc.fundraising += diocese.fundraising;
      acc.trading += diocese.trading;
      acc.investment += diocese.investment;
      acc.statutoryFees += diocese.statutoryFees;
      acc.other += diocese.other;
      return acc;
    }, {
      totalGiving: 0, taxRecovered: 0, legacies: 0, grants: 0,
      fundraising: 0, trading: 0, investment: 0, statutoryFees: 0, other: 0
    });

    return [
      { name: 'Total Giving', value: totalsBySource.totalGiving, color: '#8884d8' },
      { name: 'Statutory Fees', value: totalsBySource.statutoryFees, color: '#82ca9d' },
      { name: 'Grants', value: totalsBySource.grants, color: '#ffc658' },
      { name: 'Trading', value: totalsBySource.trading, color: '#ff7300' },
      { name: 'Tax Recovered', value: totalsBySource.taxRecovered, color: '#00ff00' },
      { name: 'Legacies', value: totalsBySource.legacies, color: '#0088fe' },
      { name: 'Fundraising', value: totalsBySource.fundraising, color: '#ff8042' },
      { name: 'Investment', value: totalsBySource.investment, color: '#8dd1e1' },
      { name: 'Other', value: totalsBySource.other, color: '#d084d0' }
    ].sort((a, b) => b.value - a.value);
  }, []);

  const scatterData = useMemo(() => {
    return rawData.map(diocese => ({
      x: diocese.totalGiving,
      y: diocese.totalIncome,
      name: diocese.diocese,
      size: diocese.totalIncome / 1000
    }));
  }, []);

  const treemapData = useMemo(() => {
    return sortedData.slice(0, 15).map(diocese => ({
      name: diocese.diocese,
      value: diocese.totalIncome,
      fill: `hsl(${(diocese.totalIncome / 1400)}, 70%, 50%)`
    }));
  }, [sortedData]);

  const formatCurrency = (value) => {
    return `�${(value / 1000).toFixed(1)}M`;
  };

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 border border-gray-300 rounded shadow-lg">
          <p className="font-semibold">{label}</p>
          {payload.map((entry, index) => (
            <p key={index} style={{ color: entry.color }}>
              {entry.name}: {formatCurrency(entry.value)}
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  const CustomScatterTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div className="bg-white p-3 border border-gray-300 rounded shadow-lg">
          <p className="font-semibold">{data.name}</p>
          <p>Total Giving: {formatCurrency(data.x)}</p>
          <p>Total Income: {formatCurrency(data.y)}</p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="w-full min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          Diocese Income Analysis 2023
        </h1>
        
        {/* Navigation */}
        <div className="flex flex-wrap justify-center gap-4 mb-8">
          {[
            { key: 'ranking', label: 'Income Ranking' },
            { key: 'sources', label: 'Income Sources' },
            { key: 'scatter', label: 'Giving vs Income' },
            { key: 'treemap', label: 'Income Distribution' }
          ].map(({ key, label }) => (
            <button
              key={key}
              onClick={() => setSelectedView(key)}
              className={`px-6 py-3 rounded-lg font-medium transition-all duration-200 ${
                selectedView === key
                  ? 'bg-blue-600 text-white shadow-lg'
                  : 'bg-white text-gray-700 hover:bg-gray-50 shadow-md'
              }`}
            >
              {label}
            </button>
          ))}
        </div>

        {/* Key Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-semibold text-gray-700">Total Income</h3>
            <p className="text-3xl font-bold text-blue-600">
              �{(rawData.reduce((sum, d) => sum + d.totalIncome, 0) / 1000000).toFixed(1)}B
            </p>
          </div>
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-semibold text-gray-700">Dioceses</h3>
            <p className="text-3xl font-bold text-green-600">{rawData.length}</p>
          </div>
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-semibold text-gray-700">Average Income</h3>
            <p className="text-3xl font-bold text-purple-600">
              �{(rawData.reduce((sum, d) => sum + d.totalIncome, 0) / rawData.length / 1000).toFixed(1)}M
            </p>
          </div>
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-semibold text-gray-700">Top Diocese</h3>
            <p className="text-2xl font-bold text-orange-600">{sortedData[0].diocese}</p>
          </div>
        </div>

        {/* Charts */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          {selectedView === 'ranking' && (
            <div>
              <h2 className="text-2xl font-bold mb-6 text-gray-800">Top 10 Dioceses by Total Income</h2>
              <ResponsiveContainer width="100%" height={500}>
                <BarChart data={top10Data} margin={{ top: 20, right: 30, left: 40, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis 
                    dataKey="diocese" 
                    angle={-45}
                    textAnchor="end"
                    height={120}
                    interval={0}
                  />
                  <YAxis tickFormatter={formatCurrency} />
                  <Tooltip content={<CustomTooltip />} />
                  <Bar dataKey="totalIncome" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          )}

          {selectedView === 'sources' && (
            <div>
              <h2 className="text-2xl font-bold mb-6 text-gray-800">Income Sources Breakdown</h2>
              <ResponsiveContainer width="100%" height={500}>
                <PieChart>
                  <Pie
                    data={incomeSourceData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(1)}%`}
                    outerRadius={180}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {incomeSourceData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip formatter={(value) => formatCurrency(value)} />
                </PieChart>
              </ResponsiveContainer>
            </div>
          )}

          {selectedView === 'scatter' && (
            <div>
              <h2 className="text-2xl font-bold mb-6 text-gray-800">Total Giving vs Total Income</h2>
              <ResponsiveContainer width="100%" height={500}>
                <ScatterChart data={scatterData} margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                  <CartesianGrid />
                  <XAxis 
                    type="number" 
                    dataKey="x" 
                    name="Total Giving"
                    tickFormatter={formatCurrency}
                  />
                  <YAxis 
                    type="number" 
                    dataKey="y" 
                    name="Total Income"
                    tickFormatter={formatCurrency}
                  />
                  <Tooltip content={<CustomScatterTooltip />} />
                  <Scatter dataKey="y" fill="#8884d8" />
                </ScatterChart>
              </ResponsiveContainer>
            </div>
          )}

          {selectedView === 'treemap' && (
            <div>
              <h2 className="text-2xl font-bold mb-6 text-gray-800">Income Distribution (Top 15 Dioceses)</h2>
              <ResponsiveContainer width="100%" height={500}>
                <Treemap
                  data={treemapData}
                  dataKey="value"
                  ratio={4/3}
                  stroke="#fff"
                  fill="#8884d8"
                  content={({ root, depth, x, y, width, height, index, name, value }) => {
                    return (
                      <g>
                        <rect
                          x={x}
                          y={y}
                          width={width}
                          height={height}
                          style={{
                            fill: `hsl(${(value / 1400)}, 70%, 50%)`,
                            stroke: '#fff',
                            strokeWidth: 2,
                          }}
                        />
                        {width > 60 && height > 30 && (
                          <>
                            <text x={x + width / 2} y={y + height / 2 - 10} textAnchor="middle" fill="#fff" fontSize="12" fontWeight="bold">
                              {name}
                            </text>
                            <text x={x + width / 2} y={y + height / 2 + 10} textAnchor="middle" fill="#fff" fontSize="10">
                              {formatCurrency(value)}
                            </text>
                          </>
                        )}
                      </g>
                    );
                  }}
                />
              </ResponsiveContainer>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default DioceseDashboard;
