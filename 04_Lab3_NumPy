{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "id": "77eea2fe-86ee-41dc-bc84-07dcf6ad4598",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "77eea2fe-86ee-41dc-bc84-07dcf6ad4598",
        "outputId": "1db3410c-2717-465e-fea2-2e48a00432c9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "----- BEFORE PCA -----\n",
            "Accuracy BEFORE PCA: 0.9629629629629629\n",
            "\n",
            "----- AFTER PCA -----\n",
            "Accuracy AFTER PCA: 0.9814814814814815\n",
            "\n",
            "Explained Variance Ratio: [0.36196226 0.18763862]\n"
          ]
        }
      ],
      "source": [
        "# ==============================\n",
        "# STEP 1: Import Required Libraries\n",
        "# ==============================\n",
        "\n",
        "from sklearn.datasets import load_wine\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.decomposition import PCA\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# STEP 2: Load Dataset\n",
        "# ==============================\n",
        "\n",
        "data = load_wine()\n",
        "\n",
        "#  Fill here\n",
        "X = data.data\n",
        "y = data.target\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# STEP 3: Split the Dataset\n",
        "# ==============================\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "   X, y, test_size=0.3, random_state=42\n",
        ")\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# STEP 4: Standardize the Data\n",
        "# ==============================\n",
        "\n",
        "scaler = StandardScaler()\n",
        "\n",
        "#  Fill here\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# PART A: BEFORE PCA\n",
        "# ==============================\n",
        "\n",
        "print(\"----- BEFORE PCA -----\")\n",
        "\n",
        "knn = KNeighborsClassifier(n_neighbors=5)\n",
        "\n",
        "# Fill here\n",
        "knn.fit(X_train_scaled, y_train)\n",
        "\n",
        "y_pred_before = knn.predict(X_test_scaled)\n",
        "acc_before = accuracy_score(y_test, y_pred_before)\n",
        "print(\"Accuracy BEFORE PCA:\", acc_before)\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# PART B: APPLY PCA\n",
        "# ==============================\n",
        "\n",
        "pca = PCA(n_components=2)\n",
        "\n",
        "# Fill here\n",
        "X_train_pca = pca.fit_transform(X_train_scaled)\n",
        "X_test_pca = pca.transform(X_test_scaled)\n",
        "\n",
        "# ==============================\n",
        "# PART C: AFTER PCA\n",
        "# ==============================\n",
        "\n",
        "print(\"\\n----- AFTER PCA -----\")\n",
        "\n",
        "knn_pca = KNeighborsClassifier(n_neighbors=5)\n",
        "\n",
        "#  Fill here\n",
        "knn_pca.fit(X_train_pca, y_train)\n",
        "\n",
        "y_pred_after = knn_pca.predict(X_test_pca)\n",
        "acc_after = accuracy_score(y_test, y_pred_after)\n",
        "\n",
        "print(\"Accuracy AFTER PCA:\", acc_after)\n",
        "\n",
        "\n",
        "# ==============================\n",
        "# BONUS: Explained Variance\n",
        "# ==============================\n",
        "\n",
        "print(\"\\nExplained Variance Ratio:\", pca.explained_variance_ratio_)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.11.7"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
